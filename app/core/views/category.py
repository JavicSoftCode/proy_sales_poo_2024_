from app.security.mixins.mixins import CreateViewMixin, DeleteViewMixin, ListViewMixin, PermissionMixin, UpdateViewMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from app.core.forms.category import CategoryForm
from app.core.models import Category
from django.contrib import messages
from django.urls import reverse_lazy
from django.db.models import Q


class CategoryListView(PermissionMixin, ListViewMixin, ListView):
  model = Category
  template_name = 'core/categories/list.html'
  context_object_name = 'category'
  permission_required = 'view_category'

  def get_queryset(self):
    q1 = self.request.GET.get('q')
    if q1:
      query = Q(description__icontains=q1)
    else:
      query = Q(active=True)

    return self.model.objects.filter(query).order_by('id')


class CategoryCreateView(PermissionMixin, CreateViewMixin, CreateView):
  model = Category
  form_class = CategoryForm
  template_name = 'core/categories/form.html'
  success_url = reverse_lazy('core:category_list')
  permission_required = 'add_category'

  def form_valid(self, form):
    response = super().form_valid(form)
    category = self.object
    messages.success(self.request, f"Éxito al crear la categoría {category.description}.")
    return response


class CategoryUpdateView(PermissionMixin, UpdateViewMixin, UpdateView):
  model = Category
  form_class = CategoryForm
  template_name = 'core/categories/form.html'
  success_url = reverse_lazy('core:category_list')
  permission_required = 'change_category'

  def form_valid(self, form):
    response = super().form_valid(form)
    category = self.object
    messages.success(self.request, f"Éxito al actualizar la categoría {category.description}.")
    return response


class CategoryDeleteView(PermissionMixin, DeleteViewMixin, DeleteView):
  model = Category
  template_name = 'core/delete.html'
  success_url = reverse_lazy('core:category_list')
  permission_required = 'delete_category'

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.object = None

  def delete(self, request, *args, **kwargs):
    self.object = self.get_object()
    success_message = f"Éxito al eliminar la categoría {self.object.description}."
    self.object.delete()
    messages.success(self.request, success_message)
    return super().delete(request, *args, **kwargs)
