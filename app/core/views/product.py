from app.security.mixins.mixins import CreateViewMixin, DeleteViewMixin, ListViewMixin, PermissionMixin, UpdateViewMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from app.core.forms.product import ProductForm
from app.core.models import Product
from django.contrib import messages
from django.urls import reverse_lazy
from django.db.models import Q
from django.http import JsonResponse


# vista para el buscadador dinamico
class ProductSuggestionsView(ListView):
  def get(self, request, *args, **kwargs):
    term = request.GET.get('term', '')
    suggestions = Product.objects.filter(description__icontains=term).values('description', 'stock', 'active')[
                  :10]
    suggestions_list = list(suggestions)
    return JsonResponse(suggestions_list, safe=False)


class ProductListView(PermissionMixin, ListViewMixin, ListView):
  model = Product
  template_name = 'core/products/list.html'
  context_object_name = 'products'
  permission_required = 'view_product'

  def get_queryset(self):
    q1 = self.request.GET.get('q')
    if q1:
      query = Q(description__icontains=q1)
    else:
      query = Q(active=True)

    return self.model.objects.filter(query).order_by('id')


class ProductCreateView(PermissionMixin, CreateViewMixin, CreateView):
  model = Product
  form_class = ProductForm
  template_name = 'core/products/form.html'
  success_url = reverse_lazy('core:product_list')
  permission_required = 'add_product'

  def form_valid(self, form):
    response = super().form_valid(form)
    product = self.object
    messages.success(self.request, f"Éxito al crear el producto {product.description}.")
    return response


class ProductUpdateView(PermissionMixin, UpdateViewMixin, UpdateView):
  model = Product
  form_class = ProductForm
  template_name = 'core/products/form.html'
  success_url = reverse_lazy('core:product_list')
  permission_required = 'change_product'

  def form_valid(self, form):
    response = super().form_valid(form)
    product = self.object
    messages.success(self.request, f"Éxito al actualizar el producto {product.description}.")
    return response


class ProductDeleteView(PermissionMixin, DeleteViewMixin, DeleteView):
  model = Product
  template_name = 'core/delete.html'
  success_url = reverse_lazy('core:product_list')
  permission_required = 'delete_product'

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.object = None

  def delete(self, request, *args, **kwargs):
    self.object = self.get_object()
    success_message = f"Éxito al eliminar el producto {self.object.description}."
    self.object.delete()
    messages.success(self.request, success_message)
    return super().delete(request, *args, **kwargs)
