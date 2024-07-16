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

<<<<<<< HEAD
=======
  # def get_context_data(self, **kwargs):
  #   context = super().get_context_data(**kwargs)
  #   queryset = self.get_queryset()
  #   paginator = Paginator(queryset, self.paginate_by)
  #
  #   page = self.request.GET.get('page')
  #   try:
  #     paymentMethod = paginator.page(page)
  #   except PageNotAnInteger:
  #     paymentMethod = paginator.page(1)
  #   except EmptyPage:
  #     paymentMethod = paginator.page(paginator.num_pages)
  #
  #   context['paymentMethod'] = paymentMethod
  #   context['title1'] = 'Método de Pago'
  #   context['title2'] = 'Consulta del método de pago'
  #   context['create_url'] = reverse_lazy('core:paymentMethod_create')
  #   context['query'] = self.request.GET.get('q', '')
  #   return context

>>>>>>> 748233b376cadbaee22ab464bb0b0ac354bcffa6

class PaymentMethodCreateView(PermissionMixin, CreateViewMixin, CreateView):
  model = PaymentMethod
  form_class = PaymentMethodForm
  template_name = 'core/paymentMethod/form.html'
  success_url = reverse_lazy('core:paymentMethod_list')
<<<<<<< HEAD
  permission_required = 'add_paymentmethod'
=======
  permission_required = 'add_paymentMethod'

  # def get_context_data(self, **kwargs):
  #   context = super().get_context_data(**kwargs)
  #   context['title1'] = 'Crear Método de Pago'
  #   context['title2'] = 'Método de Pago'
  #   context['back_url'] = self.success_url
  #   return context
>>>>>>> 748233b376cadbaee22ab464bb0b0ac354bcffa6

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

<<<<<<< HEAD
=======
  # def get_context_data(self, **kwargs):
  #   context = super().get_context_data(**kwargs)
  #   context['title1'] = 'Actualizar Método de Pago'
  #   context['title2'] = 'Actualizar Datos Del Método Pago'
  #   context['back_url'] = self.success_url
  #   return context

>>>>>>> 748233b376cadbaee22ab464bb0b0ac354bcffa6
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

<<<<<<< HEAD
=======
  # def get_context_data(self, **kwargs):
  #   context = super().get_context_data(**kwargs)
  #   context['title'] = 'Eliminar Método de Pago'
  #   context['description'] = f"¿Desea eliminar el método de pago: {self.object.description}?"
  #   context['back_url'] = self.success_url
  #   return context

>>>>>>> 748233b376cadbaee22ab464bb0b0ac354bcffa6
  def delete(self, request, *args, **kwargs):
    self.object = self.get_object()
    success_message = f"Éxito al eliminar el método de pago {self.object.description}."
    self.object.delete()
    messages.success(self.request, success_message)
    return super().delete(request, *args, **kwargs)
