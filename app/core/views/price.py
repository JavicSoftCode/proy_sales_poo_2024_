from django.db.models.query import QuerySet
from django.urls import reverse_lazy
from app.core.forms.price import ProductPriceForm
from app.core.models import ProductPrice
from app.security.instance.menu_module import MenuModule
from app.security.mixins.mixins import CreateViewMixin, ListViewMixin, PermissionMixin, UpdateViewMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib import messages
from django.db.models import Q


# -- Price Product CLASS -- #
class ProductPriceListView(PermissionMixin, ListViewMixin, ListView):
  template_name = 'core/price/list.html'
  model = ProductPrice
  context_object_name = "precios"
  permission_required = "view_productprice"

  def get_queryset(self):
    q1 = self.request.GET.get('q')
    if q1:
      query = Q(line__description__icontains=q1)
    else:
      query = Q(active=True)

    return self.model.objects.filter(query).order_by('id')


class ProductPriceCreateView(PermissionMixin, CreateViewMixin, CreateView):
  model = ProductPrice
  template_name = 'core/price/form.html'
  form_class = ProductPriceForm
  success_url = reverse_lazy('core:price_list')
  permission_required = 'add_productprice'
  print(form_class)


class ProductPriceUpdateView(PermissionMixin, UpdateViewMixin, UpdateView):
  model = ProductPrice
  template_name = 'core/price/form.html'
  form_class = ProductPriceForm
  success_url = reverse_lazy('core:price_list')
  permission_required = 'change_productprice'

  def form_valid(self, form):
    response = super().form_valid(form)
    price = self.object
    messages.success(self.request, f"Éxito al actualizar la Precio del producto {price.category}.")
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
