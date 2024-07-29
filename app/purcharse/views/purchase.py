# from io import BytesIO
# import json
# from django.http import JsonResponse, HttpResponse
# from django.db import transaction
# from django.urls import reverse_lazy, reverse
# from django.utils import timezone
# from django.views.generic import CreateView, ListView, UpdateView, DeleteView, View, TemplateView
# from django.contrib import messages
# from django.db.models import Q, F
# from decimal import Decimal
# from datetime import timedelta
# from datetime import date
# from django.shortcuts import redirect, get_object_or_404, render
# from django.template.loader import get_template
# from xhtml2pdf import pisa
# from app.core.models import Product, Supplier
# from app.purcharse.forms import PurchaseForm
# from app.purcharse.models import Purchase, PurchaseDetail
# from app.security.mixins.mixins import PermissionMixin, CreateViewMixin, UpdateViewMixin, ListViewMixin
# from proy_sales.utils import custom_serializer, save_audit
#
# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
#
#
# class PurchaseListView(PermissionMixin, ListViewMixin, ListView):
#   template_name = 'purchase/list.html'
#   model = Purchase
#   context_object_name = 'purchases'
#   permission_required = 'view_purchase'
#
#   def get_queryset(self):
#     self.query = Q()
#     q1 = self.request.GET.get('q')
#     if q1 is not None:
#       self.query.add(Q(id=q1), Q.OR)
#       self.query.add(Q(supplier__name__icontains=q1), Q.OR)
#       # Incluir tanto activos como inactivos si hay una búsqueda
#       return self.model.objects.filter(self.query).order_by('id')
#     else:
#       # Solo incluye registros activos si no hay búsqueda
#       return self.model.objects.filter(Q(active=True)).order_by('id')
#
#   def get_context_data(self, **kwargs):
#     context = super().get_context_data(**kwargs)
#     queryset = self.get_queryset()
#     context['now'] = timezone.now()
#     paginator = Paginator(queryset, self.paginate_by)
#
#     purchase = self.request.GET.get('purchase')
#     try:
#       purchaese = paginator.page(purchase)
#     except PageNotAnInteger:
#       purchaese = paginator.page(1)
#     except EmptyPage:
#       purchaese = paginator.page(paginator.num_pages)
#
#     context['purchases'] = purchaese
#     context['title1'] = 'IC - Compras'
#     context['title2'] = 'Consulta de las Compras'
#     context['create_url'] = reverse_lazy('purchase:purchase_create')
#     context['query'] = self.request.GET.get('q', '')
#     return context
#
#
# class PurchaseCreateView(PermissionMixin, CreateViewMixin, CreateView):
#   model = Purchase
#   template_name = 'purchase/form.html'
#   form_class = PurchaseForm
#   success_url = reverse_lazy('purchase:purchase_list')
#   permission_required = 'add_purchase'
#
#   def get_context_data(self, **kwargs):
#     context = super().get_context_data(**kwargs)
#     context['products'] = Product.active_products.values('id', 'description', 'price', 'stock', 'iva__value')
#     context['detail_purchases'] = []
#     context['title1'] = 'IC - Compras'
#     context['title2'] = 'Crear una nueva compra'
#     context['save_url'] = reverse_lazy('purcharse:purchase_create')
#     return context
#
#   def post(self, request, *args, **kwargs):
#     form = self.get_form()
#     if not form.is_valid():
#       messages.success(self.request, f"Error al registrar la compra: {form.errors}.")
#       return JsonResponse({"msg": form.errors}, status=400)
#     data = request.POST
#     try:
#       with transaction.atomic():
#         purchase = Purchase.objects.create(
#           supplier_id=int(data['supplier']),
#           issue_date=data['issue_date'],
#           subtotal=Decimal(data['subtotal']),
#           iva=Decimal(data['iva']),
#           total=Decimal(data['total'])
#         )
#         details = json.loads(request.POST['detail'])
#         for detail in details:
#           product = Product.objects.get(id=int(detail['id']))
#           product.stock += Decimal(detail['quantify'])
#           product.save()
#           PurchaseDetail.objects.create(
#             purchase=purchase,
#             product=product,
#             quantify=Decimal(detail['quantify']),
#             cost=Decimal(detail['price']),
#             iva=Decimal(detail['iva']),
#             subtotal=Decimal(detail['sub'])
#           )
#         save_audit(request, purchase, "A")
#         messages.success(self.request, f"Éxito al registrar la compra N#{purchase.id}")
#         return JsonResponse({"msg": "Éxito al registrar la compra"}, status=200)
#     except Exception as ex:
#       return JsonResponse({"msg": str(ex)}, status=400)
#
#
# class PurchaseUpdateView(PermissionMixin, UpdateViewMixin, UpdateView):
#   model = Purchase
#   template_name = 'purchase/form.html'
#   form_class = PurchaseForm
#   success_url = reverse_lazy('purchase:purchase_list')
#   permission_required = 'change_purchase'
#
#   def get_context_data(self, **kwargs):
#     context = super().get_context_data(**kwargs)
#     context['products'] = Product.active_products.values('id', 'description', 'price', 'stock', 'iva__value')
#     detail_purchase = list(PurchaseDetail.objects.filter(purchase_id=self.object.id).values(
#       "product", "product__description", "quantify", "cost", "subtotal", "iva"))
#     detail_purchase = json.dumps(detail_purchase, default=custom_serializer)
#     context['detail_purchases'] = detail_purchase
#     context['title1'] = 'IC - Compras'
#     context['title2'] = 'Actualiza tus Compras'
#     context['save_url'] = reverse_lazy('purcharse:purchase_update', kwargs={"pk": self.object.id})
#     return context
#
#   def post(self, request, *args, **kwargs):
#     form = self.get_form()
#     if not form.is_valid():
#       messages.success(self.request, f"Error al actualizar la compra: {form.errors}.")
#       return JsonResponse({"msg": form.errors}, status=400)
#     data = request.POST
#     try:
#       purchase = Purchase.objects.get(id=self.kwargs.get('pk'))
#       with transaction.atomic():
#         purchase.supplier_id = int(data['supplier'])
#         purchase.issue_date = data['issue_date']
#         purchase.subtotal = Decimal(data['subtotal'])
#         purchase.iva = Decimal(data['iva'])
#         purchase.total = Decimal(data['total'])
#         purchase.save()
#
#         # Restablecer el stock de productos a su estado anterior
#         detdelete = PurchaseDetail.objects.filter(purchase_id=purchase.id)
#         for det in detdelete:
#           det.product.stock -= int(det.quantify)
#           det.product.save()
#         detdelete.delete()
#
#         details = json.loads(request.POST['detail'])
#         for detail in details:
#           product = Product.objects.get(id=int(detail['id']))
#           product.stock += Decimal(detail['quantify'])
#           product.save()
#           PurchaseDetail.objects.create(
#             purchase=purchase,
#             product=product,
#             quantify=Decimal(detail['quantify']),
#             cost=Decimal(detail['price']),
#             iva=Decimal(detail['iva']),
#             subtotal=Decimal(detail['sub'])
#           )
#         save_audit(request, purchase, "M")
#         messages.success(self.request, f"Éxito al modificar la compra N#{purchase.id}")
#         return JsonResponse({"msg": "Éxito al modificar la compra"}, status=200)
#     except Exception as ex:
#       return JsonResponse({"msg": str(ex)}, status=400)
#
#
# from django.db import IntegrityError
#
#
# class PurchaseCancelView(View):
#   def post(self, request, *args, **kwargs):
#     purchase = get_object_or_404(Purchase, id=kwargs['pk'])
#     if purchase.state != 'A':
#       purchase.state = 'A'  # Cambia el estado a anulado
#       purchase.save()
#       messages.success(request, "Compra anulada con éxito.")
#     else:
#       messages.error(request, "La compra ya está anulada.")
#     return redirect(reverse('purcharse:purchase_list'))
#
#
# class PurchaseDeleteView(View):
#   success_url = reverse_lazy('purchase:purchase_list')
#
#   def post(self, request, *args, **kwargs):
#     purchase = get_object_or_404(Purchase, id=kwargs['pk'])
#     # Verifica si la fecha de emisión es menor a 3 días
#     if timezone.now() - purchase.issue_date <= timezone.timedelta(days=3):
#       try:
#         purchase.active = False  # Realiza la eliminación lógica
#         purchase.save()
#         messages.success(request, "Compra eliminada con éxito.")
#       except Exception as e:
#         messages.error(request, f"No se pudo eliminar la compra: {str(e)}")
#     else:
#       messages.error(request, "La compra no puede ser eliminada porque ha pasado más de 3 días.")
#     return redirect(reverse('purchase:purchase_list'))
#
#
# class PurchaseConsultView(TemplateView):
#   template_name = 'purchase/consult.html'
#
#   def get_context_data(self, **kwargs):
#     context = super().get_context_data(**kwargs)
#     purchase_id = self.kwargs.get('pk')
#     purchase = get_object_or_404(Purchase, pk=purchase_id)
#     context['purchase'] = purchase
#     context['details'] = purchase.purchase_detail.all()
#     return context
#
#
# def generate_purchase_pdf(request, purchase_id):
#   purchase = get_object_or_404(Purchase, id=purchase_id)
#   template = get_template('purchase/pdfgenerate.html')
#   context = {
#     'purchase': purchase,
#   }
#   html = template.render(context)
#   result = BytesIO()
#   pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
#   if not pdf.err:
#     response = HttpResponse(result.getvalue(), content_type='application/pdf')
#     filename = f"purchase_{purchase_id}.pdf"
#     content = f"attachment; filename={filename}"
#     response['Content-Disposition'] = content
#     return response
#   return HttpResponse("Error generando el PDF", status=400)

from io import BytesIO
import json
from django.http import JsonResponse, HttpResponse
from django.db import transaction
from django.urls import reverse_lazy, reverse
from django.utils import timezone
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, View, TemplateView
from django.contrib import messages
from django.db.models import Q
from decimal import Decimal
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import redirect, get_object_or_404
from django.template.loader import get_template
from xhtml2pdf import pisa
from app.core.models import Product, Supplier
from app.purcharse.forms import PurchaseForm
from app.purcharse.models import Purchase, PurchaseDetail
from app.security.mixins.mixins import PermissionMixin, CreateViewMixin, UpdateViewMixin, ListViewMixin
from proy_sales.utils import custom_serializer, save_audit


class PurchaseSuggestionsView(ListView):
  def get(self, request, *args, **kwargs):
    term = request.GET.get('term', '')
    suggestions = Purchase.objects.filter(id__icontains=term).values(
      'id',
      'supplier__name',
      'supplier__ruc',
      'state',
      'active'
    )[:10]
    suggestions_list = [
      {
        'id': item['id'],
        'supplier': item['supplier__name'],
        'supplier_ruc': item['supplier__ruc'],
        'state': item['state'],
        'active': item['active']
      } for item in suggestions
    ]
    return JsonResponse(suggestions_list, safe=False)


class PurchaseListView(PermissionMixin, ListViewMixin, ListView):
  template_name = 'purchase/list.html'
  model = Purchase
  context_object_name = 'purchases'
  permission_required = 'view_purchase'

  def get_queryset(self):
    self.query = Q()
    q1 = self.request.GET.get('q')
    if q1 is not None:
      self.query.add(Q(id=q1), Q.OR)
      self.query.add(Q(supplier__name__icontains=q1), Q.OR)
      return self.model.objects.filter(self.query).order_by('id')
    else:
      return self.model.objects.filter(Q(active=True)).order_by('id')

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    queryset = self.get_queryset()
    context['now'] = timezone.now()
    paginator = Paginator(queryset, self.paginate_by)

    purchase = self.request.GET.get('purchase')
    try:
      purchases = paginator.page(purchase)
    except PageNotAnInteger:
      purchases = paginator.page(1)
    except EmptyPage:
      purchases = paginator.page(paginator.num_pages)

    context['purchases'] = purchases
    context['title1'] = 'IC - Compras'
    context['title2'] = 'Consulta de las Compras'
    context['create_url'] = reverse_lazy('purchase:purchase_create')
    context['query'] = self.request.GET.get('q', '')
    return context


class PurchaseCreateView(PermissionMixin, CreateViewMixin, CreateView):
  model = Purchase
  template_name = 'purchase/form.html'
  form_class = PurchaseForm
  success_url = reverse_lazy('purchase:purchase_list')
  permission_required = 'add_purchase'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['products'] = Product.active_products.values('id', 'description', 'price', 'stock', 'iva__value')
    context['detail_purchases'] = []
    context['title1'] = 'IC - Compras'
    context['title2'] = 'Crear una nueva compra'
    context['save_url'] = reverse_lazy('purchase:purchase_create')
    return context

  def post(self, request, *args, **kwargs):
    form = self.get_form()
    if not form.is_valid():
      messages.error(self.request, f"Error al registrar la compra: {form.errors}.")
      return JsonResponse({"msg": form.errors}, status=400)
    data = request.POST
    try:
      with transaction.atomic():
        purchase = Purchase.objects.create(
          supplier_id=int(data['supplier']),
          issue_date=data['issue_date'],
          subtotal=Decimal(data['subtotal']),
          iva=Decimal(data['iva']),
          total=Decimal(data['total'])
        )
        details = json.loads(request.POST['detail'])
        for detail in details:
          product = Product.objects.get(id=int(detail['id']))
          product.stock += Decimal(detail['quantify'])
          product.save()
          PurchaseDetail.objects.create(
            purchase=purchase,
            product=product,
            quantify=Decimal(detail['quantify']),
            cost=Decimal(detail['price']),
            iva=Decimal(detail['iva']),
            subtotal=Decimal(detail['sub'])
          )
        save_audit(request, purchase, "A")
        messages.success(self.request, f"Éxito al registrar la compra N#{purchase.id}")
        return JsonResponse({"msg": "Éxito al registrar la compra"}, status=200)
    except Exception as ex:
      return JsonResponse({"msg": str(ex)}, status=400)


class PurchaseUpdateView(PermissionMixin, UpdateViewMixin, UpdateView):
  model = Purchase
  template_name = 'purchase/form.html'
  form_class = PurchaseForm
  success_url = reverse_lazy('purchase:purchase_list')
  permission_required = 'change_purchase'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['products'] = Product.active_products.values('id', 'description', 'price', 'stock', 'iva__value')
    detail_purchase = list(PurchaseDetail.objects.filter(purchase_id=self.object.id).values(
      "product", "product__description", "quantify", "cost", "subtotal", "iva"))
    detail_purchase = json.dumps(detail_purchase, default=custom_serializer)
    context['detail_purchases'] = detail_purchase
    context['title1'] = 'IC - Compras'
    context['title2'] = 'Actualiza tus Compras'
    context['save_url'] = reverse_lazy('purchase:purchase_update', kwargs={"pk": self.object.id})
    return context

  def post(self, request, *args, **kwargs):
    form = self.get_form()
    if not form.is_valid():
      messages.error(self.request, f"Error al actualizar la compra: {form.errors}.")
      return JsonResponse({"msg": form.errors}, status=400)
    data = request.POST
    try:
      purchase = Purchase.objects.get(id=self.kwargs.get('pk'))
      with transaction.atomic():
        purchase.supplier_id = int(data['supplier'])
        purchase.issue_date = data['issue_date']
        purchase.subtotal = Decimal(data['subtotal'])
        purchase.iva = Decimal(data['iva'])
        purchase.total = Decimal(data['total'])
        purchase.save()

        # Restablecer el stock de productos a su estado anterior
        detdelete = PurchaseDetail.objects.filter(purchase_id=purchase.id)
        for det in detdelete:
          det.product.stock -= int(det.quantify)
          det.product.save()
        detdelete.delete()

        details = json.loads(request.POST['detail'])
        for detail in details:
          product = Product.objects.get(id=int(detail['id']))
          product.stock += Decimal(detail['quantify'])
          product.save()
          PurchaseDetail.objects.create(
            purchase=purchase,
            product=product,
            quantify=Decimal(detail['quantify']),
            cost=Decimal(detail['price']),
            iva=Decimal(detail['iva']),
            subtotal=Decimal(detail['sub'])
          )
        save_audit(request, purchase, "M")
        messages.success(self.request, f"Éxito al modificar la compra N#{purchase.id}")
        return JsonResponse({"msg": "Éxito al modificar la compra"}, status=200)
    except Exception as ex:
      return JsonResponse({"msg": str(ex)}, status=400)


class PurchaseCancelView(View):
  def post(self, request, *args, **kwargs):
    purchase = get_object_or_404(Purchase, id=kwargs['pk'])
    if purchase.state != 'A':
      purchase.state = 'A'  # Cambia el estado a anulado
      purchase.save()
      messages.success(request, "Compra anulada con éxito.")
    else:
      messages.error(request, "La compra ya está anulada.")
    return redirect(reverse('purchase:purchase_list'))


class PurchaseDeleteView(View):
  success_url = reverse_lazy('purchase:purchase_list')

  def post(self, request, *args, **kwargs):
    purchase = get_object_or_404(Purchase, id=kwargs['pk'])
    # Verifica si la fecha de emisión es menor a 3 días
    if timezone.now() - purchase.issue_date <= timezone.timedelta(days=3):
      try:
        purchase.active = False  # Realiza la eliminación lógica
        purchase.save()
        messages.success(request, "Compra eliminada con éxito.")
      except Exception as e:
        messages.error(request, f"No se pudo eliminar la compra: {str(e)}")
    else:
      messages.error(request, "La compra no puede ser eliminada porque ha pasado más de 3 días.")
    return redirect(reverse('purchase:purchase_list'))


class PurchaseConsultView(TemplateView):
  template_name = 'purchase/consult.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    purchase_id = self.kwargs.get('pk')
    purchase = get_object_or_404(Purchase, pk=purchase_id)
    context['purchase'] = purchase
    context['details'] = purchase.purchase_detail.all()
    return context


def generate_purchase_pdf(request, purchase_id):
  purchase = get_object_or_404(Purchase, id=purchase_id)
  template = get_template('purchase/pdfgenerate.html')
  context = {
    'purchase': purchase,
  }
  html = template.render(context)
  result = BytesIO()
  pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
  if not pdf.err:
    response = HttpResponse(result.getvalue(), content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="purchase_{purchase.id}.pdf"'
    return response
  return HttpResponse("Error al generar el PDF.", status=400)
