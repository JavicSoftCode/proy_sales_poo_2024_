from app.security.mixins.mixins import CreateViewMixin, ListViewMixin, PermissionMixin, UpdateViewMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from app.core.forms.price import ProductPriceForm
from app.core.models import ProductPrice
from django.db.models.query import QuerySet
from django.contrib import messages
from django.urls import reverse_lazy
from django.db.models import Q
from django.http import JsonResponse


# vista para el buscadador dinamico
class ProductPriceSuggestionsView(ListView):
    def get(self, request, *args, **kwargs):
        term = request.GET.get('term', '')
        suggestions = ProductPrice.objects.filter(
            Q(product__description__icontains=term)  # Aquí suponemos que 'name' es el campo relevante en 'Product'
        ).values('product__name', 'active')[:10]
        suggestions_list = list(suggestions)
        return JsonResponse(suggestions_list, safe=False)


class ProductPriceListView(PermissionMixin, ListViewMixin, ListView):
  model = ProductPrice
  template_name = 'core/price/list.html'
  context_object_name = "precios"
  permission_required = "view_productprice"

  def get_queryset(self):
    q1 = self.request.GET.get('q')
    if q1:
      query = Q(product__description__icontains=q1)  # Aquí ajustamos la búsqueda
    else:
      query = Q(active=True)

    return self.model.objects.filter(query).order_by('id')


class ProductPriceCreateView(PermissionMixin, CreateViewMixin, CreateView):
  model = ProductPrice
  form_class = ProductPriceForm
  template_name = 'core/price/form.html'
  success_url = reverse_lazy('core:price_list')
  permission_required = 'add_productprice'

  def form_valid(self, form):
    response = super().form_valid(form)
    price = self.object
    messages.success(self.request, f"Éxito al crear el nuevo Precio del producto {price.product}.")
    return response


class ProductPriceUpdateView(PermissionMixin, UpdateViewMixin, UpdateView):
  model = ProductPrice
  form_class = ProductPriceForm
  template_name = 'core/price/form.html'
  success_url = reverse_lazy('core:price_list')
  permission_required = 'change_productprice'

  def form_valid(self, form):
    response = super().form_valid(form)
    price = self.object
    messages.success(self.request, f"Éxito al actualizar la Precio del producto {price.product}.")
    return response


class ProductPriceDeleteView(PermissionMixin, DeleteView):
  model = ProductPrice
  template_name = 'core/price/delete.html'
  success_url = reverse_lazy('core:price_list')
  permission_required = 'delete_productprice'

  def delete(self, request, *args, **kwargs):
    price = self.get_object()
    price.active = False
    price.save()
    messages.success(request, f"Éxito al eliminar el Precio del producto {price.description}.")
    return super().delete(request, *args, **kwargs)
