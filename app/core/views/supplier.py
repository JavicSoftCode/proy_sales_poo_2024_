from app.security.mixins.mixins import CreateViewMixin, DeleteViewMixin, ListViewMixin, PermissionMixin, UpdateViewMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from app.core.forms.supplier import SupplierForm
from app.core.models import Supplier
from django.contrib import messages
from django.urls import reverse_lazy
from django.db.models import Q


class SupplierListView(PermissionMixin, ListViewMixin, ListView):
  model = Supplier
  template_name = 'core/suppliers/list.html'
  context_object_name = 'suppliers'
  permission_required = 'view_supplier'

  def get_queryset(self):
    q1 = self.request.GET.get('q')
    if q1:
      query = Q(ruc__icontains=q1)
    else:
      query = Q(active=True)

    return self.model.objects.filter(query).order_by('id')


class SupplierCreateView(PermissionMixin, CreateViewMixin, CreateView):
  model = Supplier
  form_class = SupplierForm
  template_name = 'core/suppliers/form.html'
  success_url = reverse_lazy('core:supplier_list')
  permission_required = 'add_supplier'

  def form_valid(self, form):
    response = super().form_valid(form)
    supplier = self.object
    messages.success(self.request, f"Éxito al crear al proveedor {supplier.name}.")
    return response


class SupplierUpdateView(PermissionMixin, UpdateViewMixin, UpdateView):
  model = Supplier
  form_class = SupplierForm
  template_name = 'core/suppliers/form.html'
  success_url = reverse_lazy('core:supplier_list')
  permission_required = 'change_supplier'

  def form_valid(self, form):
    response = super().form_valid(form)
    supplier = self.object
    messages.success(self.request, f"Éxito al actualizar el proveedor {supplier.name}.")
    return response


class SupplierDeleteView(PermissionMixin, DeleteViewMixin, DeleteView):
  model = Supplier
  template_name = 'core/delete.html'
  success_url = reverse_lazy('core:supplier_list')
  permission_required = 'delete_supplier'

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.object = None

  def delete(self, request, *args, **kwargs):
    self.object = self.get_object()
    success_message = f"Éxito al eliminar lógicamente la marca {self.object.description}."
    self.object.delete()
    messages.success(self.request, success_message)
    return super().delete(request, *args, **kwargs)
