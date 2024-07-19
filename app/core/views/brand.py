from app.security.mixins.mixins import CreateViewMixin, DeleteViewMixin, ListViewMixin, PermissionMixin, UpdateViewMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from app.core.forms.brand import BrandForm
from app.core.models import Brand
from django.contrib import messages
from django.urls import reverse_lazy
from django.db.models import Q
from django.http import JsonResponse


# vista para el buscadador dinamico
class BrandSuggestionsView(ListView):
  def get(self, request, *args, **kwargs):
    term = request.GET.get('term', '')
    suggestions = Brand.objects.filter(description__icontains=term).values('description', 'active')[
                  :10]
    suggestions_list = list(suggestions)
    return JsonResponse(suggestions_list, safe=False)


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


class BrandCreateView(PermissionMixin, CreateViewMixin, CreateView):
  model = Brand
  form_class = BrandForm
  template_name = 'core/brands/form.html'
  success_url = reverse_lazy('core:brand_list')
  permission_required = 'add_brand'

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

  def delete(self, request, *args, **kwargs):
    self.object = self.get_object()
    success_message = f"Éxito al eliminar la marca {self.object.description}."
    self.object.delete()
    messages.success(self.request, success_message)
    return super().delete(request, *args, **kwargs)
