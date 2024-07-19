from app.security.mixins.mixins import CreateViewMixin, DeleteViewMixin, ListViewMixin, PermissionMixin, UpdateViewMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from app.core.forms.customer import CustomerForm
from app.core.models import Customer
from django.contrib import messages
from django.urls import reverse_lazy
from django.db.models import Q
from django.shortcuts import render
from django.http import JsonResponse
from folium.plugins import FastMarkerCluster
import folium


# vista para el buscadador dinamico
class CustomerSuggestionsView(ListView):
  def get(self, request, *args, **kwargs):
    term = request.GET.get('term', '')
    suggestions = Customer.objects.filter(dni__icontains=term).values('dni', 'first_name', 'last_name', 'active')[
                  :10]
    suggestions_list = list(suggestions)
    return JsonResponse(suggestions_list, safe=False)


class CustomerListView(PermissionMixin, ListViewMixin, ListView):
  model = Customer
  template_name = 'core/customers/list.html'
  context_object_name = 'customers'
  permission_required = 'view_customer'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)

    locations = self.get_queryset()

    locations_data = [
      {
        'latitude': location.latitude,
        'longitude': location.longitude,
        'first_name': location.first_name,
        'last_name': location.last_name,
        'address': location.address,
        'image': location.image.url
      }
      for location in locations
    ]

    context['locations'] = locations_data
    context['title1'] = "Clientes"
    context['encabezado'] = "Todas las ubicaciones de los Clientes"
    return context

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

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)

    locations = Customer.objects.all()

    initial_map = folium.Map(location=[-2.129896, -79.593256], zoom_start=14)

    latitudes = [location.latitude for location in locations]
    longitudes = [location.longitude for location in locations]
    popups = [f"<b>{location.first_name} {location.last_name}</b><br>{location.address}" for location in locations]

    FastMarkerCluster(data=list(zip(latitudes, longitudes, popups))).add_to(initial_map)

    for location in locations:
      folium.Marker(
        location=[location.latitude, location.longitude],
        popup=f"<b>{location.first_name} {location.last_name}</b><br>{location.address}",
        icon=folium.Icon(icon='user', prefix='fa')
      ).add_to(initial_map)

    context['map'] = initial_map._repr_html_()
    context['locations'] = locations
    context['title2'] = "Registrar Cliente"
    context['encabezado'] = "Ubicación Cliente"
    return context

  def form_valid(self, form):
    response = super().form_valid(form)
    customer = self.object
    messages.success(self.request, f"Éxito al crear el cliente {customer.get_full_name}.")
    return response


class CustomerUpdateView(PermissionMixin, UpdateViewMixin, UpdateView):
  model = Customer
  form_class = CustomerForm
  template_name = 'core/customers/updateform.html'
  success_url = reverse_lazy('core:customer_list')
  permission_required = 'change_customer'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    customer = self.object

    locations = Customer.objects.all()

    initial_map = folium.Map(location=[customer.latitude, customer.longitude], zoom_start=14)

    latitudes = [location.latitude for location in locations]
    longitudes = [location.longitude for location in locations]
    popups = [f"<b>{location.first_name} {location.last_name}</b><br>{location.address}" for location in locations]

    FastMarkerCluster(data=list(zip(latitudes, longitudes, popups))).add_to(initial_map)

    for location in locations:
      folium.Marker(
        location=[location.latitude, location.longitude],
        popup=f"<b>{location.first_name} {location.last_name}</b><br>{location.address}",
        icon=folium.Icon(icon='user', prefix='fa')
      ).add_to(initial_map)

    folium.Marker(
      location=[customer.latitude, customer.longitude],
      popup=f"<b>{customer.first_name} {customer.last_name}</b><br>{customer.address}",
      icon=folium.Icon(icon='user', prefix='fa', color='blue')
    ).add_to(initial_map)

    context['map'] = initial_map._repr_html_()
    context['locations'] = locations
    context['title2'] = "Actualizar Cliente"
    context['encabezado'] = "Ubicación Cliente"
    return context

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
