<<<<<<< HEAD
from app.security.mixins.mixins import CreateViewMixin, ListViewMixin, PermissionMixin, UpdateViewMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from app.core.forms.price import ProductPriceForm
from app.core.models import ProductPrice
from django.db.models.query import QuerySet
from django.contrib import messages
from django.urls import reverse_lazy
from django.db.models import Q


class ProductPriceListView(PermissionMixin, ListViewMixin, ListView):
  model = ProductPrice
  template_name = 'core/price/list.html'
=======
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
>>>>>>> 748233b376cadbaee22ab464bb0b0ac354bcffa6
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
<<<<<<< HEAD
  form_class = ProductPriceForm
  template_name = 'core/price/form.html'
  success_url = reverse_lazy('core:price_list')
  permission_required = 'add_productprice'

  def form_valid(self, form):
    response = super().form_valid(form)
    price = self.object
    messages.success(self.request, f"Éxito al crear el nuevo Precio del producto {price.product}.")
    return response
=======
  template_name = 'core/price/form.html'
  form_class = ProductPriceForm
  success_url = reverse_lazy('core:price_list')
  permission_required = 'add_productprice'
  print(form_class)
>>>>>>> 748233b376cadbaee22ab464bb0b0ac354bcffa6


class ProductPriceUpdateView(PermissionMixin, UpdateViewMixin, UpdateView):
  model = ProductPrice
<<<<<<< HEAD
  form_class = ProductPriceForm
  template_name = 'core/price/form.html'
=======
  template_name = 'core/price/form.html'
  form_class = ProductPriceForm
>>>>>>> 748233b376cadbaee22ab464bb0b0ac354bcffa6
  success_url = reverse_lazy('core:price_list')
  permission_required = 'change_productprice'

  def form_valid(self, form):
    response = super().form_valid(form)
    price = self.object
<<<<<<< HEAD
    messages.success(self.request, f"Éxito al actualizar la Precio del producto {price.product}.")
=======
    messages.success(self.request, f"Éxito al actualizar la Precio del producto {price.category}.")
>>>>>>> 748233b376cadbaee22ab464bb0b0ac354bcffa6
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
