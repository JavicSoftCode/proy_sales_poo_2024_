from django.urls import reverse_lazy
from app.core.forms.product import ProductForm
from app.core.models import Product
from app.security.instance.menu_module import MenuModule
from app.security.mixins.mixins import CreateViewMixin, DeleteViewMixin, ListViewMixin, PermissionMixin, UpdateViewMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib import messages
from django.db.models import Q


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

  # def get_context_data(self, **kwargs):
  #   context = super().get_context_data(**kwargs)
  #   queryset = self.get_queryset()
  #   paginator = Paginator(queryset, self.paginate_by)
  #
  #   page = self.request.GET.get('page')
  #   try:
  #     products = paginator.page(page)
  #   except PageNotAnInteger:
  #     products = paginator.page(1)
  #   except EmptyPage:
  #     products = paginator.page(paginator.num_pages)
  #
  #   context['brands'] = products
  #   context['title1'] = 'Productos'
  #   context['title2'] = 'Consulta de Productos'
  #   context['create_url'] = reverse_lazy('core:product_create')
  #   context['query'] = self.request.GET.get('q', '')
  #   return context


class ProductCreateView(PermissionMixin, CreateViewMixin, CreateView):
  model = Product
  form_class = ProductForm
  template_name = 'core/products/form.html'
  success_url = reverse_lazy('core:product_list')
  permission_required = 'add_product'

  # def get_context_data(self, **kwargs):
  #   context = super().get_context_data(**kwargs)
  #   context['title1'] = 'Crear Producto'
  #   context['title2'] = 'Producto'
  #   context['back_url'] = self.success_url
  #   return context

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

  # def get_context_data(self, **kwargs):
  #   context = super().get_context_data(**kwargs)
  #   context['title1'] = 'Actualizar Producto'
  #   context['title2'] = 'Actualizar Datos Del Producto'
  #   context['back_url'] = self.success_url
  #   return context

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

  # def get_context_data(self, **kwargs):
  #   context = super().get_context_data(**kwargs)
  #   context['title'] = 'Eliminar Producto'
  #   context['description'] = f"¿Desea eliminar el producto: {self.object.description}?"
  #   context['back_url'] = self.success_url
  #   return context

  def delete(self, request, *args, **kwargs):
    self.object = self.get_object()
    success_message = f"Éxito al eliminar el producto {self.object.description}."
    self.object.delete()
    messages.success(self.request, success_message)
    return super().delete(request, *args, **kwargs)
