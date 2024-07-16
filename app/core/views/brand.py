from app.security.mixins.mixins import CreateViewMixin, DeleteViewMixin, ListViewMixin, PermissionMixin, UpdateViewMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from app.core.forms.brand import BrandForm
from app.core.models import Brand
from django.contrib import messages
from django.urls import reverse_lazy
from django.db.models import Q


class BrandListView(PermissionMixin, ListViewMixin, ListView):
  model = Brand
  template_name = 'core/brands/list.html'
  context_object_name = 'brands'
  permission_required = 'view_brand'

  def get_queryset(self):
    q1 = self.request.GET.get('q')
    if q1:
      query = Q(description__icontains=q1)
    else:
      query = Q(active=True)

    return self.model.objects.filter(query).order_by('id')

<<<<<<< HEAD
=======
  # def get_context_data(self, **kwargs):
  #   context = super().get_context_data(**kwargs)
  #   queryset = self.get_queryset()
  #   paginator = Paginator(queryset, self.paginate_by)
  #
  #   page = self.request.GET.get('page')
  #   try:
  #     brands = paginator.page(page)
  #   except PageNotAnInteger:
  #     brands = paginator.page(1)
  #   except EmptyPage:
  #     brands = paginator.page(paginator.num_pages)
  #
  #   context['brands'] = brands
  #   context['title1'] = 'Marcas'
  #   context['title2'] = 'Consulta de Marcas'
  #   context['create_url'] = reverse_lazy('core:brand_create')
  #   context['query'] = self.request.GET.get('q', '')
  #   return context

>>>>>>> 748233b376cadbaee22ab464bb0b0ac354bcffa6

class BrandCreateView(PermissionMixin, CreateViewMixin, CreateView):
  model = Brand
  form_class = BrandForm
  template_name = 'core/brands/form.html'
  success_url = reverse_lazy('core:brand_list')
  permission_required = 'add_brand'

<<<<<<< HEAD
=======
  # def get_context_data(self, **kwargs):
  #   context = super().get_context_data(**kwargs)
  #   context['title1'] = 'Crear Marca'
  #   context['title2'] = 'Marca'
  #   context['back_url'] = self.success_url
  #   return context

>>>>>>> 748233b376cadbaee22ab464bb0b0ac354bcffa6
  def form_valid(self, form):
    response = super().form_valid(form)
    brand = self.object
    messages.success(self.request, f"Éxito al crear la marca {brand.description}.")
    return response


class BrandUpdateView(PermissionMixin, UpdateViewMixin, UpdateView):
  model = Brand
  form_class = BrandForm
  template_name = 'core/brands/form.html'
  success_url = reverse_lazy('core:brand_list')
  permission_required = 'change_brand'

<<<<<<< HEAD
=======
  # def get_context_data(self, **kwargs):
  #   context = super().get_context_data(**kwargs)
  #   context['title1'] = 'Actualizar Marca'
  #   context['title2'] = 'Actualizar Datos De La Marca'
  #   context['back_url'] = self.success_url
  #   return context

>>>>>>> 748233b376cadbaee22ab464bb0b0ac354bcffa6
  def form_valid(self, form):
    response = super().form_valid(form)
    brand = self.object
    messages.success(self.request, f"Éxito al actualizar la marca {brand.description}.")
    return response


class BrandDeleteView(PermissionMixin, DeleteViewMixin, DeleteView):
  model = Brand
  template_name = 'core/delete.html'
  success_url = reverse_lazy('core:brand_list')
  permission_required = 'delete_brand'

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.object = None

<<<<<<< HEAD
=======
  # def get_context_data(self, **kwargs):
  #   context = super().get_context_data(**kwargs)
  #   context['title'] = 'Eliminar Marca'
  #   context['description'] = f"¿Desea eliminar la marca: {self.object.description}?"
  #   context['back_url'] = self.success_url
  #   return context

>>>>>>> 748233b376cadbaee22ab464bb0b0ac354bcffa6
  def delete(self, request, *args, **kwargs):
    self.object = self.get_object()
    success_message = f"Éxito al eliminar la marca {self.object.description}."
    self.object.delete()
    messages.success(self.request, success_message)
    return super().delete(request, *args, **kwargs)
