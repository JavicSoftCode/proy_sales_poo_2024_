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
<<<<<<< HEAD
=======

  # def get_queryset(self):
  #   q = self.request.GET.get('q')
  #   queryset = self.model.objects.all().order_by('id')  # Todos los clientes
  #
  #   if q:
  #     queryset = queryset.filter(Q(dni__icontains=q) | Q(first_name__icontains=q) | Q(last_name__icontains=q))
  #
  #   return queryset
>>>>>>> 748233b376cadbaee22ab464bb0b0ac354bcffa6

  def get_queryset(self):
    q1 = self.request.GET.get('q')
    if q1:
      query = Q(dni__icontains=q1)
    else:
      query = Q(active=True)

    return self.model.objects.filter(query).order_by('id')
<<<<<<< HEAD
=======

  # def get_context_data(self, **kwargs):
  #   context = super().get_context_data(**kwargs)
  #   queryset = self.get_queryset()
  #
  #   # Filtrar por clientes activos si no hay búsqueda
  #   if not self.request.GET.get('q'):
  #     queryset = queryset.filter(active=True)
  #
  #   paginator = Paginator(queryset, self.paginate_by)
  #
  #   page = self.request.GET.get('page')
  #   try:
  #     customers = paginator.page(page)
  #   except PageNotAnInteger:
  #     customers = paginator.page(1)
  #   except EmptyPage:
  #     customers = paginator.page(paginator.num_pages)
  #
  #   context['customers'] = customers
  #   context['title1'] = 'Clientes'
  #   context['title2'] = 'Consulta de Clientes'
  #   context['create_url'] = reverse_lazy('core:customer_create')
  #   context['query'] = self.request.GET.get('q', '')
  #   return context
>>>>>>> 748233b376cadbaee22ab464bb0b0ac354bcffa6


class CustomerCreateView(PermissionMixin, CreateViewMixin, CreateView):
  model = Customer
  form_class = CustomerForm
  template_name = 'core/customers/form.html'
  success_url = reverse_lazy('core:customer_list')
  permission_required = 'add_customer'

<<<<<<< HEAD
=======
  # def get_context_data(self, **kwargs):
  #   context = super().get_context_data(**kwargs)
  #   context['title1'] = 'Crear Cliente'
  #   context['title2'] = 'Cliente'
  #   context['back_url'] = self.success_url
  #   return context

>>>>>>> 748233b376cadbaee22ab464bb0b0ac354bcffa6
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

<<<<<<< HEAD
=======
  # def get_context_data(self, **kwargs):
  #   context = super().get_context_data(**kwargs)
  #   context['title1'] = 'Actualizar Cliente'
  #   context['title2'] = 'Actualizar Datos Del Cliente'
  #   context['back_url'] = self.success_url
  #   return context

>>>>>>> 748233b376cadbaee22ab464bb0b0ac354bcffa6
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

<<<<<<< HEAD
=======
  # def get_context_data(self, **kwargs):
  #   context = super().get_context_data(**kwargs)
  #   context['title'] = 'Eliminar Cliente'
  #   context['description'] = f"¿Desea eliminar el cliente: {self.object.get_full_name}?"
  #   context['back_url'] = self.success_url
  #   return context

>>>>>>> 748233b376cadbaee22ab464bb0b0ac354bcffa6
  def delete(self, request, *args, **kwargs):
    self.object = self.get_object()
    success_message = f"Éxito al eliminar el cliente {self.object.get_full_name}."
    self.object.delete()
    messages.success(self.request, success_message)
    return super().delete(request, *args, **kwargs)
