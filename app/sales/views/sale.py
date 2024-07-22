from decimal import Decimal
from io import BytesIO
import json
from datetime import timedelta
from django.http import JsonResponse, HttpResponse
from django.db import transaction
from django.urls import reverse_lazy
from django.utils import timezone
from django.shortcuts import get_object_or_404, redirect, render
from django.template.loader import get_template
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from xhtml2pdf import pisa
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, View, TemplateView, DetailView
from django.contrib import messages
from django.db.models import Q

from app.core.forms.supplier import SupplierForm
from app.core.models import Product, Company
from app.sales.forms.invoice import InvoiceForm
from app.sales.models import Invoice, InvoiceDetail
from app.security.mixins.mixins import CreateViewMixin, DeleteViewMixin, ListViewMixin, PermissionMixin, UpdateViewMixin
from proy_sales.utils import custom_serializer, save_audit


class SalesSuggestionsView(ListView):
  def get(self, request, *args, **kwargs):
    term = request.GET.get('term', '')
    suggestions = Invoice.objects.filter(id__icontains=term).values(
      'id',
      'customer__first_name',
      'customer__last_name',
      'state',
      'active'
    )[:10]
    suggestions_list = [
      {
        'id': item['id'],
        'customer': item['customer__first_name'],
        'customer_last': item['customer__last_name'],
        'state': item['state'],
        'active': item['active']
      } for item in suggestions
    ]
    return JsonResponse(suggestions_list, safe=False)


class SaleListView(PermissionMixin, ListViewMixin, ListView):
  template_name = 'sales/invoices/list.html'
  model = Invoice
  context_object_name = 'invoices'
  permission_required = 'view_invoice'

  def get_queryset(self):
    query = Q(active=True)
    search_query = self.request.GET.get('q')
    if search_query:
      try:
        invoice_id = int(search_query)
        return self.model.objects.filter(Q(id=invoice_id)).order_by('id')
      except ValueError:
        query.add(Q(customer__first_name__icontains=search_query), Q.OR)
        query.add(Q(customer__last_name__icontains=search_query), Q.OR)
    return self.model.objects.filter(query).order_by('id')

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    queryset = self.get_queryset()
    paginator = Paginator(queryset, self.paginate_by)

    page = self.request.GET.get('page')
    try:
      sales = paginator.page(page)
    except PageNotAnInteger:
      sales = paginator.page(1)
    except EmptyPage:
      sales = paginator.page(paginator.num_pages)

    context['sales'] = sales
    context['title1'] = 'Ventas'
    context['title2'] = 'Consulta de las Ventas'
    context['create_url'] = reverse_lazy('sales:sales_create')
    context['query'] = self.request.GET.get('q', '')
    return context


class SaleCreateView(PermissionMixin, CreateViewMixin, CreateView):
  model = Invoice
  template_name = 'sales/invoices/form.html'
  form_class = InvoiceForm
  success_url = reverse_lazy('sales:invoice_list')
  permission_required = 'add_invoice'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['products'] = Product.active_products.values('id', 'description', 'price', 'stock', 'iva__value')
    context['detail_sales'] = []
    context['save_url'] = reverse_lazy('sales:sales_create')
    context['title1'] = 'Venta'
    context['title2'] = 'Registrar Venta'
    context['create_url'] = reverse_lazy('purcharse:purchase_create')
    context['query'] = self.request.GET.get('q', '')
    return context

  def post(self, request, *args, **kwargs):
    form = self.get_form()
    if not form.is_valid():
      messages.error(self.request, f"Error al grabar la venta: {form.errors}.")
      return JsonResponse({"msg": form.errors}, status=400)
    data = request.POST
    try:
      with transaction.atomic():
        sale = Invoice.objects.create(
          customer_id=int(data['customer']),
          payment_method_id=int(data['payment_method']),
          issue_date=data['issue_date'],
          subtotal=Decimal(data['subtotal']),
          discount=Decimal(data['discount']),
          iva=Decimal(data['iva']),
          total=Decimal(data['total']),
          payment=Decimal(data['payment']),
          change=Decimal(data['change']),
          state='N'
        )
        details = json.loads(request.POST['detail'])
        for detail in details:
          inv_det = InvoiceDetail.objects.create(
            invoice=sale,
            product_id=int(detail['id']),
            quantity=Decimal(detail['quantify']),
            price=Decimal(detail['price']),
            iva=Decimal(detail['iva']),
            subtotal=Decimal(detail['sub'])
          )
          inv_det.product.reduce_stock(Decimal(detail['quantify']))
        save_audit(request, sale, "N")
        messages.success(self.request, f"Éxito al registrar la venta F#{sale.id}")
        return JsonResponse({"msg": "Éxito al registrar la venta Factura"}, status=200)
    except Exception as ex:
      return JsonResponse({"msg": str(ex)}, status=400)


class SaleUpdateView(PermissionMixin, UpdateViewMixin, UpdateView):
  model = Invoice
  template_name = 'sales/invoices/form.html'
  form_class = InvoiceForm
  success_url = reverse_lazy('sales:invoice_list')
  permission_required = 'change_invoice'

  def get_context_data(self, **kwargs):
    context = super().get_context_data()
    context['products'] = Product.active_products.values('id', 'description', 'price', 'stock', 'iva__value')
    detail_sale = list(InvoiceDetail.objects.filter(invoice_id=self.object.id).values(
      "product", "product__description", "quantity", "price", "subtotal", "iva"))
    detail_sale = json.dumps(detail_sale, default=custom_serializer)
    context['detail_sales'] = detail_sale
    context['title1'] = "Ventas"
    context['save_url'] = reverse_lazy('sales:sales_update', kwargs={"pk": self.object.id})
    return context

  def post(self, request, *args, **kwargs):
    form = self.get_form()
    if not form.is_valid():
      messages.success(self.request, f"Error al actualizar la venta: {form.errors}.")
      return JsonResponse({"msg": form.errors}, status=400)
    data = request.POST
    try:
      sale = Invoice.objects.get(id=self.kwargs.get('pk'))
      with transaction.atomic():
        sale.customer_id = int(data['customer'])
        sale.payment_method_id = int(data['payment_method'])
        sale.issue_date = data['issue_date']
        sale.subtotal = Decimal(data['subtotal'])
        sale.discount = Decimal(data['discount'])
        sale.iva = Decimal(data['iva'])
        sale.total = Decimal(data['total'])
        sale.payment = Decimal(data['payment'])
        sale.change = Decimal(data['change'])
        sale.state = 'M'
        sale.save()
        details = json.loads(request.POST['detail'])
        detdelete = InvoiceDetail.objects.filter(invoice_id=sale.id)
        for det in detdelete:
          det.product.stock += int(det.quantity)
          det.product.save()
        detdelete.delete()

        for detail in details:
          inv_det = InvoiceDetail.objects.create(
            invoice=sale,
            product_id=int(detail['id']),
            quantity=Decimal(detail['quantify']),
            price=Decimal(detail['price']),
            iva=Decimal(detail['iva']),
            subtotal=Decimal(detail['sub'])
          )
          inv_det.product.reduce_stock(Decimal(detail['quantify']))
        save_audit(request, sale, "M")
        messages.success(self.request, f"Éxito al Modificar la venta F#{sale.id}")
        return JsonResponse({"msg": "Éxito al Modificar la venta Factura"}, status=200)
    except Exception as ex:
      return JsonResponse({"msg": ex}, status=400)


class SaleCancelView(PermissionMixin, View):
  template_name = 'sales/invoices/cancel.html'
  permission_required = 'delete_invoice'

  def post(self, request, *args, **kwargs):
    try:
      sale = Invoice.objects.get(id=self.kwargs.get('pk'))
      if sale.state == 'A':
        messages.error(self.request, "LA VENTA YA ESTÁ ANULADA")
        return redirect('sales:sales_list')
      current_time = timezone.now()
      time_difference = current_time - sale.issue_date
      if time_difference > timedelta(days=3):
        messages.error(self.request, "La venta ya no puede ser anulada, pasaron los días establecidos")
        return redirect('sales:sales_list')
      with transaction.atomic():
        sale.state = 'A'
        sale.save()
        details = InvoiceDetail.objects.filter(invoice_id=sale.id)
        for detail in details:
          product = detail.product
          product.stock += detail.quantity
          product.save()
        save_audit(request, sale, "A")
        messages.success(self.request, f"Éxito al anular la venta F#{sale.id}")
        return redirect('sales:sales_list')
    except Invoice.DoesNotExist:
      messages.error(self.request, "Factura No encontrada")
      return redirect('sales:sales_list')
    except Exception as ex:
      return JsonResponse({"msg": str(ex)}, status=400)


class SaleDeleteView(PermissionMixin, View):
  permission_required = 'delete_invoice'

  def post(self, request, *args, **kwargs):
    try:
      sale = Invoice.objects.get(id=self.kwargs.get('pk'))
      current_time = timezone.now()
      if not sale.active:
        messages.error(self.request, "Error al eliminar la venta, ya está desactivada")
        return redirect('sales:sales_list')
      if (current_time - sale.issue_date).days > 3:
        messages.error(self.request, "La venta no puede ser eliminada después de 3 días.")
        return redirect('sales:sales_list')
      sale.active = False
      sale.save()
      save_audit(request, sale, "D")
      messages.success(self.request, f"Éxito al eliminar la venta F#{sale.id}")
      return redirect('sales:sales_list')
    except Invoice.DoesNotExist:
      messages.error(self.request, "Factura No encontrada")
      return redirect('sales:sales_list')
    except Exception as ex:
      return JsonResponse({"msg": str(ex)}, status=400)


def generate_invoice_pdf(request, invoice_id):
  invoice = get_object_or_404(Invoice, id=invoice_id)
  company = Company.objects.filter(id=1)

  template = get_template('sales/invoices/pdfgenera.html')
  context = {
    'invoice': invoice,
    'company': company,
  }
  html = template.render(context)

  result = BytesIO()
  pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result, encoding='UTF-8')

  if not pdf.err:
    response = HttpResponse(result.getvalue(), content_type='application/pdf')
    filename = f"invoice_{invoice_id}.pdf"
    content = f"inline; filename={filename}"
    response['Content-Disposition'] = content
    return response

  return HttpResponse("Error generando el PDF", status=400)


class SalesConsultView(TemplateView):
  template_name = 'sales/invoices/consult.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    invoice_id = self.kwargs.get('pk')
    invoice = get_object_or_404(Invoice, pk=invoice_id)
    company = Company.objects.filter(id=1)
    print(company)
    context['company'] = company
    context['invoice'] = invoice
    return context
