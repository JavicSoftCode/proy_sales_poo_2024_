from app.security.mixins.mixins import CreateViewMixin, DeleteViewMixin, ListViewMixin, PermissionMixin, UpdateViewMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from app.core.forms.paymentMethod import PaymentMethodForm
from app.core.models import PaymentMethod
from django.contrib import messages
from django.urls import reverse_lazy
from django.db.models import Q


class PaymentMethodListView(PermissionMixin, ListViewMixin, ListView):
  model = PaymentMethod
  template_name = 'core/paymentMethod/list.html'
  context_object_name = 'paymentMethod'
  permission_required = 'view_paymentMethod'

  def get_queryset(self):
    q1 = self.request.GET.get('q')
    if q1:
      query = Q(description__icontains=q1)
    else:
      query = Q(active=True)

    return self.model.objects.filter(query).order_by('id')


class PaymentMethodCreateView(PermissionMixin, CreateViewMixin, CreateView):
  model = PaymentMethod
  form_class = PaymentMethodForm
  template_name = 'core/paymentMethod/form.html'
  success_url = reverse_lazy('core:paymentMethod_list')
  permission_required = 'add_paymentmethod'

  def form_valid(self, form):
    response = super().form_valid(form)
    PaymentMethod = self.object
    messages.success(self.request, f"Éxito al crear el método de pago {PaymentMethod.description}.")
    return response


class PaymentMethodUpdateView(PermissionMixin, UpdateViewMixin, UpdateView):
  model = PaymentMethod
  form_class = PaymentMethodForm
  template_name = 'core/paymentMethod/form.html'
  success_url = reverse_lazy('core:paymentMethod_list')
  permission_required = 'change_paymentMethod'

  def form_valid(self, form):
    response = super().form_valid(form)
    PaymentMethod = self.object
    messages.success(self.request, f"Éxito al actualizar el método de pago {PaymentMethod.description}.")
    return response


class PaymentMethodDeleteView(PermissionMixin, DeleteViewMixin, DeleteView):
  model = PaymentMethod
  template_name = 'core/delete.html'
  success_url = reverse_lazy('core:paymentMethod_list')
  permission_required = 'delete_paymentMethod'

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.object = None

  def delete(self, request, *args, **kwargs):
    self.object = self.get_object()
    success_message = f"Éxito al eliminar el método de pago {self.object.description}."
    self.object.delete()
    messages.success(self.request, success_message)
    return super().delete(request, *args, **kwargs)
