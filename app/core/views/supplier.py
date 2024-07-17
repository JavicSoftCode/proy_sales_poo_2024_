from app.security.mixins.mixins import CreateViewMixin, DeleteViewMixin, ListViewMixin, PermissionMixin, UpdateViewMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from app.core.forms.supplier import SupplierForm
from app.core.models import Supplier
from django.contrib import messages
from django.urls import reverse_lazy
from django.db.models import Q
from django.shortcuts import render
import folium
from folium.plugins import FastMarkerCluster


class SupplierListView(PermissionMixin, ListViewMixin, ListView):
  model = Supplier
  template_name = 'core/suppliers/list.html'
  context_object_name = 'suppliers'
  permission_required = 'view_supplier'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)

    locations = self.get_queryset()

    locations_data = [
      {
        'latitude': location.latitude,
        'longitude': location.longitude,
        'name': location.name,
        'address': location.address,
        'image': location.image.url
      }
      for location in locations
    ]

    context['locations'] = locations_data
    context['encabezado'] = "Todas las ubicaciones de los Proveedores"
    return context

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

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)

    locations = Supplier.objects.all()

    initial_map = folium.Map(location=[-2.129896, -79.593256], zoom_start=14)

    latitudes = [location.latitude for location in locations]
    longitudes = [location.longitude for location in locations]
    popups = [f"<b>{location.name}</b><br>{location.address}" for location in locations]

    FastMarkerCluster(data=list(zip(latitudes, longitudes, popups))).add_to(initial_map)

    for location in locations:
      folium.Marker(
        location=[location.latitude, location.longitude],
        popup=f"<b>{location.name}</b><br>{location.address}",
        icon=folium.Icon(icon='user', prefix='fa')
      ).add_to(initial_map)

    context['map'] = initial_map._repr_html_()
    context['locations'] = locations
    context['title2'] = "Registrar Proveedor"
    context['encabezado'] = "Ubicación Proveedor"
    return context

  def form_valid(self, form):
    response = super().form_valid(form)
    supplier = self.object
    messages.success(self.request, f"Éxito al crear al proveedor {supplier.name}.")
    return response


class SupplierUpdateView(PermissionMixin, UpdateViewMixin, UpdateView):
  model = Supplier
  form_class = SupplierForm
  template_name = 'core/suppliers/updateform.html'
  success_url = reverse_lazy('core:supplier_list')
  permission_required = 'change_supplier'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    supplier = self.object

    locations = Supplier.objects.all()

    initial_map = folium.Map(location=[supplier.latitude, supplier.longitude], zoom_start=14)

    latitudes = [location.latitude for location in locations]
    longitudes = [location.longitude for location in locations]
    popups = [f"<b>{location.name}</b><br>{location.address}" for location in locations]

    FastMarkerCluster(data=list(zip(latitudes, longitudes, popups))).add_to(initial_map)

    for location in locations:
      folium.Marker(
        location=[location.latitude, location.longitude],
        popup=f"<b>{location.name}</b><br>{location.address}",
        icon=folium.Icon(icon='user', prefix='fa')
      ).add_to(initial_map)

    folium.Marker(
      location=[supplier.latitude, supplier.longitude],
      popup=f"<b>{supplier.name}</b><br>{supplier.address}",
      icon=folium.Icon(icon='user', prefix='fa', color='blue')
    ).add_to(initial_map)

    context['map'] = initial_map._repr_html_()
    context['locations'] = locations
    context['title2'] = "Actualizar Proveedor"
    context['encabezado'] = "Ubicación Proveedor"
    return context

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
