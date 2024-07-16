from app.security.mixins.mixins import CreateViewMixin, DeleteViewMixin, ListViewMixin, PermissionMixin, UpdateViewMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from app.core.forms.customer import CustomerForm
from app.core.models import Customer
from django.contrib import messages
from django.urls import reverse_lazy
from django.db.models import Q


class CustomerListView(PermissionMixin, ListViewMixin, ListView):
  model = Customer
  template_name = 'core/customers/list.html'
  context_object_name = 'customers'
  permission_required = 'view_customer'

  def get_queryset(self):
    q1 = self.request.GET.get('q')
    if q1:
      query = Q(dni__icontains=q1)
    else:
      query = Q(active=True)

    return self.model.objects.filter(query).order_by('id')


class CustomerCreateView(PermissionMixin, CreateViewMixin, CreateView):
  model = Customer
  form_class = CustomerForm
  template_name = 'core/customers/form.html'
  success_url = reverse_lazy('core:customer_list')
  permission_required = 'add_customer'

  def form_valid(self, form):
    response = super().form_valid(form)
    customer = self.object
    messages.success(self.request, f"Éxito al crear el cliente {customer.get_full_name}.")
    return response


class CustomerUpdateView(PermissionMixin, UpdateViewMixin, UpdateView):
  model = Customer
  form_class = CustomerForm
  template_name = 'core/customers/form.html'
  success_url = reverse_lazy('core:customer_list')
  permission_required = 'change_customer'

  def form_valid(self, form):
    response = super().form_valid(form)
    customer = self.object
    messages.success(self.request, f"Éxito al actualizar el cliente {customer.get_full_name}.")
    return response


class CustomerDeleteView(PermissionMixin, DeleteViewMixin, DeleteView):
  model = Customer
  template_name = 'core/delete.html'
  success_url = reverse_lazy('core:customer_list')
  permission_required = 'delete_customer'

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.object = None

  def delete(self, request, *args, **kwargs):
    self.object = self.get_object()
    success_message = f"Éxito al eliminar el cliente {self.object.get_full_name}."
    self.object.delete()
    messages.success(self.request, success_message)
    return super().delete(request, *args, **kwargs)
