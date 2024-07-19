from app.security.mixins.mixins import CreateViewMixin, DeleteViewMixin, ListViewMixin, PermissionMixin, UpdateViewMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from app.core.forms.company import CompanyForm
from app.core.models import Company
from django.contrib import messages
from django.urls import reverse_lazy
from django.db.models import Q
from django.shortcuts import render
from django.http import JsonResponse
from folium.plugins import FastMarkerCluster
import folium


# vista para el buscadador dinamico
class CompanySuggestionsView(ListView):
  def get(self, request, *args, **kwargs):
    term = request.GET.get('term', '')
    suggestions = Company.objects.filter(
      Q(dni__icontains=term) | Q(name__icontains=term)
    ).values('dni', 'name')[:10]
    suggestions_list = list(suggestions)
    return JsonResponse(suggestions_list, safe=False)


class CompanyListView(PermissionMixin, ListViewMixin, ListView):
  model = Company
  template_name = 'core/company/list.html'
  context_object_name = 'company'
  permission_required = 'view_company'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)

    locations = self.get_queryset()

    locations_data = [
      {
        'latitude': location.latitude,
        'longitude': location.longitude,
        'name': location.name,
        'address': location.address,
        'image': location.logo.url
      }
      for location in locations
    ]

    context['locations'] = locations_data
    context['title1'] = "Empresa"
    context['encabezado'] = "Todas las ubicaciones de las Empresas"
    return context

  def get_queryset(self):
    q = self.request.GET.get('q')
    queryset = self.model.objects.all().order_by('id')
    if q:
      queryset = queryset.filter(Q(dni__icontains=q) | Q(name__icontains=q))

    return queryset


class CompanyCreateView(PermissionMixin, CreateViewMixin, CreateView):
  model = Company
  form_class = CompanyForm
  template_name = 'core/company/form.html'
  success_url = reverse_lazy('core:company_list')
  permission_required = 'add_company'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)

    locations = Company.objects.all()

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
    context['title2'] = "Registrar Empresa"
    context['encabezado'] = "Ubicación Empresa"
    return context

  def form_valid(self, form):
    response = super().form_valid(form)
    company = self.object
    messages.success(self.request, f"Éxito al crear la compañía {company.name}.")
    return response


class CompanyUpdateView(PermissionMixin, UpdateViewMixin, UpdateView):
  model = Company
  form_class = CompanyForm
  template_name = 'core/company/updateform.html'
  success_url = reverse_lazy('core:company_list')
  permission_required = 'change_company'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    company = self.object

    locations = Company.objects.all()

    initial_map = folium.Map(location=[company.latitude, company.longitude], zoom_start=14)

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
      location=[company.latitude, company.longitude],
      popup=f"<b>{company.name}</b><br>{company.address}",
      icon=folium.Icon(icon='user', prefix='fa', color='blue')
    ).add_to(initial_map)

    context['map'] = initial_map._repr_html_()
    context['locations'] = locations
    context['title2'] = "Actualizar Empresa"
    context['encabezado'] = "Ubicación Empresa"
    return context

  def form_valid(self, form):
    response = super().form_valid(form)
    company = self.object
    messages.success(self.request, f"Éxito al actualizar la compañía {company.name}.")
    return response


class CompanyDeleteView(PermissionMixin, DeleteViewMixin, DeleteView):
  model = Company
  template_name = 'core/delete.html'
  success_url = reverse_lazy('core:company_list')
  permission_required = 'delete_company'

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.object = None

  def delete(self, request, *args, **kwargs):
    self.object = self.get_object()
    success_message = f"Éxito al eliminar la compañía {self.object.name}."
    self.object.required_to_keep_accounting = False
    self.object.save()
    messages.success(self.request, success_message)
    return super().delete(request, *args, **kwargs)
