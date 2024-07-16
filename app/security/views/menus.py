from app.security.mixins.mixins import CreateViewMixin, DeleteViewMixin, ListViewMixin, PermissionMixin, UpdateViewMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from app.security.models import Menu
from django.urls import reverse_lazy
from django.db.models import Q
from django.contrib import messages
from app.security.forms.menu import MenuForm


# Presentar todos los modulos
class MenuListView(PermissionMixin, ListViewMixin, ListView):
  template_name = 'security/menu/list.html'
  model = Menu
  context_object_name = 'menus'
  permission_required = 'view_menu'

  def get_queryset(self):
    q1 = self.request.GET.get('q')
    queryset = super().get_queryset()  # Obtener el queryset inicial

    if q1:
      queryset = queryset.filter(name__icontains=q1)

    return queryset.order_by('id')


class MenuCreateView(PermissionMixin, CreateViewMixin, CreateView):
  model = Menu
  template_name = 'security/menu/form.html'
  form_class = MenuForm
  success_url = reverse_lazy('security:menus_list')
  permission_required = 'add_menu'

  def form_valid(self, form):
    response = super().form_valid(form)
    menu = self.object
    messages.success(self.request, f"Éxito al crear el menu {menu.name}.")
    return response


class MenuUpdateView(PermissionMixin, UpdateViewMixin, UpdateView):
  model = Menu
  template_name = 'security/menu/form.html'
  form_class = MenuForm
  success_url = reverse_lazy('security:menus_list')
  permission_required = 'change_menu'

  def form_valid(self, form):
    response = super().form_valid(form)
    menu = self.object
    messages.success(self.request, f"Éxito al actualizar el menu {menu.name}.")
    return response


# class MenuDeleteView(PermissionMixin, DeleteViewMixin, DeleteView):
#   model = Menu
#   template_name = 'core/delete.html'
#   success_url = reverse_lazy('core:menus_list')
#   permission_required = 'delete_menu'

class MenuDeleteView(PermissionMixin, DeleteViewMixin, DeleteView):
  model = Menu
  template_name = 'core/delete.html'
  success_url = reverse_lazy('security:menus_list')
  permission_required = 'delete_menu'

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.object = None

  # def get_context_data(self, **kwargs):
  #   context = super().get_context_data(**kwargs)
  #   context['title'] = 'Eliminar Marca'
  #   context['description'] = f"¿Desea eliminar la marca: {self.object.description}?"
  #   context['back_url'] = self.success_url
  #   return context

  def delete(self, request, *args, **kwargs):
    self.object = self.get_object()
    success_message = f"Éxito al eliminar la marca {self.object.name}."
    self.object.delete()
    messages.success(self.request, success_message)
    return super().delete(request, *args, **kwargs)
