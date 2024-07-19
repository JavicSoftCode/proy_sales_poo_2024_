# from django.views.generic import ListView, CreateView, UpdateView, DeleteView
# from django.db.models import Q
# from django.urls import reverse_lazy
# from app.security.models import GroupModulePermission
# from app.security.mixins.mixins import PermissionMixin, ListViewMixin, CreateViewMixin, UpdateViewMixin, DeleteViewMixin
# from app.security.forms.group_module_permissions import GroupModulePermissionForm
# from django.contrib import messages
#
#
# class GroupModulePermissionListView(PermissionMixin, ListViewMixin, ListView):
#   template_name = 'security/group_module_permission/list.html'
#   model = GroupModulePermission
#   context_object_name = 'group_module_permissions'
#   permission_required = 'view_groupmodulepermission'
#
#   def get_queryset(self):
#     q1 = self.request.GET.get('q')
#     query = Q()
#     if q1:
#       query.add(Q(group__name__icontains=q1), Q.OR)
#       query.add(Q(module__name__icontains=q1), Q.OR)
#       query.add(Q(permissions__name__icontains=q1), Q.OR)
#     return self.model.objects.filter(query).distinct().order_by('id')
#
#   def get_context_data(self, **kwargs):
#     context = super().get_context_data(**kwargs)
#     context['create_url'] = reverse_lazy('security:group_module_permission_add')
#     return context
#
#
# class GroupModulePermissionCreateView(PermissionMixin, CreateViewMixin, CreateView):
#   model = GroupModulePermission
#   form_class = GroupModulePermissionForm
#   template_name = 'security/group_module_permission/form.html'
#   permission_required = 'add_groupmodulepermission'
#   success_url = reverse_lazy('security:group_module_permission_list')
#
#   def get_context_data(self, **kwargs):
#     context = super().get_context_data(**kwargs)
#     context['title'] = 'Grupo-Modulo-Permisos'
#     context['grabar'] = 'Grabar Grupo-Modulo-Permisos'
#     context['back_url'] = self.success_url
#     return context
#
#   def form_valid(self, form):
#     response = super().form_valid(form)
#     group_module_permission = self.object
#     messages.success(self.request, f"Éxito al crear {group_module_permission.module.name} - {group_module_permission.group.name}.")
#     return response
#
#
# class GroupModulePermissionUpdateView(PermissionMixin, UpdateViewMixin, UpdateView):
#   model = GroupModulePermission
#   template_name = 'security/group_module_permission/form.html'
#   form_class = GroupModulePermissionForm
#   success_url = reverse_lazy('security:group_module_permission_list')
#   permission_required = 'change_groupmodulepermission'
#
#   def get_context_data(self, **kwargs):
#     context = super().get_context_data(**kwargs)
#     context['title'] = 'Grupo Módulo Permiso'
#     context['grabar'] = 'Actualizar Grupo Módulo Permiso'
#     context['back_url'] = self.success_url
#     return context
#
#   def form_valid(self, form):
#     response = super().form_valid(form)
#     group_module_permission = self.object
#     messages.success(self.request,
#                      f"Éxito al actualizar el grupo módulo permiso {group_module_permission.module.name} - {group_module_permission.group.name}.")
#     return response
#
#
# class GroupModulePermissionDeleteView(PermissionMixin, DeleteViewMixin, DeleteView):
#   model = GroupModulePermission
#   template_name = 'core/delete.html'
#   success_url = reverse_lazy('security:group_module_permission_list')
#   permission_required = 'delete_groupmodulepermission'
#
#   def get_context_data(self, **kwargs):
#     context = super().get_context_data()
#     context['grabar'] = 'Eliminar Grupo-Modulo-Permisos'
#     context['name'] = f"¿Desea Eliminar el Grupo-Modulo: {self.object.module.name}?"
#     context['back_url'] = self.success_url
#     return context

from django.db.models.query import QuerySet
from django.urls import reverse_lazy
from django.shortcuts import redirect, render, get_object_or_404
from django.http import JsonResponse
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from app.security.models import GroupModulePermission, Module, Group, Permission
from app.security.forms.group_module_permissions import GroupModulePermissionForm
from app.security.mixins.mixins import CreateViewMixin, DeleteViewMixin, ListViewMixin, PermissionMixin, UpdateViewMixin
from django.contrib import messages
from django.db.models import Q


class GroupModulePermissionListView(PermissionMixin, ListViewMixin, ListView):
  template_name = 'security/group_module_permission/list.html'
  model = GroupModulePermission
  context_object_name = 'grupomodulopermisos'
  permission_required = 'view_groupmodulepermission'

  def get_queryset(self):
    q = self.request.GET.get('q')
    query = Q()
    if q:
      query = Q(group__name__icontains=q) | Q(module__name__icontains=q)
    return GroupModulePermission.objects.filter(query).order_by('-id')

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['create_url'] = reverse_lazy('security:groupmodulepermission_create')
    return context


class GroupModulePermissionCreateView(PermissionMixin, CreateViewMixin, CreateView):
  template_name = 'security/group_module_permission/form.html'
  model = GroupModulePermission
  form_class = GroupModulePermissionForm
  success_url = reverse_lazy('security:groupmodulepermission_list')
  permission_required = 'add_groupmodulepermission'

  def form_valid(self, form):
    group = form.cleaned_data['group']
    # Eliminar  todos los permisos actuales del grupo seleccionado
    GroupModulePermission.objects.filter(group=group).delete()
    modules_selected = self.request.POST.getlist('modules[]')

    for module_id in modules_selected:
      module = Module.objects.get(id=module_id)
      new_group_module_permission = GroupModulePermission.objects.create(
        group=group,
        module=module,
      )
      permissions_selected = self.request.POST.getlist(f'permissions_{module_id}[]')
      new_group_module_permission.permissions.set(permissions_selected)

    messages.success(self.request, "Permisos de grupo para los modulos seleccionados creados exitosamente.")
    print(modules_selected)
    print(redirect(self.success_url))
    return redirect(self.success_url)


class GroupModulePermissionUpdateView(PermissionMixin, UpdateViewMixin, UpdateView):
  model = GroupModulePermission
  template_name = 'security/group_module_permission/form.html'
  form_class = GroupModulePermissionForm
  success_url = reverse_lazy('security:groupmodulepermission_list')
  permission_required = 'change_groupmodulepermission'

  def get_context_data(self, **kwargs):
    context = super().get_context_data()
    context['grabar'] = 'Actualizar permisos'
    context['back_url'] = self.success_url
    return context

  def form_valid(self, form):
    response = super().form_valid(form)
    gmp = self.object
    messages.success(self.request, f"Éxito al actualizar los permisos del grupo {gmp.group.name}")
    return response


class GroupModulePermissionDeleteView(PermissionMixin, DeleteViewMixin, DeleteView):
  model = GroupModulePermission
  template_name = 'core/delete.html'
  success_url = reverse_lazy('security:groupmodulepermission_list')
  permission_required = 'delete_groupmodulepermission'

  def delete(self, request, *args, **kwargs):
    self.object = self.get_object
    self.object.delete()
    messages.success(self.request, f"Permiso de grupo para modulo' {self.object.module.name}'eliminado exitosamente.")
    return super().delete(request, *args, **kwargs)

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['description'] = f"¿Desea eliminar los permisos del grupo: {self.object.module.name}?"
    return context


def get_group_permissions(self, group_id):
  all_modules = Module.objects.all()
  group_modules_permissions = GroupModulePermission.objects.filter(group_id=group_id).select_related('module')
  assigned_modules = {gmp.module.id: list(gmp.permissions.values('id', 'name')) for gmp in group_modules_permissions}

  permissions_data = []
  for module in all_modules:
    module_data = {
      'module_id': module.id,
      'module_name': module.name,
      'permissions': list(module.permissions.values('id', 'name')),
      'assigned_permissions': assigned_modules.get(module.id, [])
    }
    permissions_data.append(module_data)
  print(JsonResponse(permissions_data, safe=False))
  return JsonResponse(permissions_data, safe=False)


def get_module_permissions(request, module_id):
  try:
    module = Module.objects.get(id=module_id)
    permissions = list(module.permissions.values('id', 'name'))
    return JsonResponse(permissions, safe=False)
  except Module.DoesNotExist:
    return JsonResponse({'error': 'Module not found'}, status=404)