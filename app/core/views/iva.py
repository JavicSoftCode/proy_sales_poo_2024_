<<<<<<< HEAD
from app.security.mixins.mixins import CreateViewMixin, DeleteViewMixin, ListViewMixin, PermissionMixin, UpdateViewMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from app.core.forms.iva import IvaForm
from app.core.models import Iva
from django.contrib import messages
from django.urls import reverse_lazy
=======
from django.urls import reverse_lazy
from app.core.forms.iva import IvaForm
from app.core.models import Iva
from app.security.instance.menu_module import MenuModule
from app.security.mixins.mixins import CreateViewMixin, DeleteViewMixin, ListViewMixin, PermissionMixin, UpdateViewMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib import messages
>>>>>>> 748233b376cadbaee22ab464bb0b0ac354bcffa6
from django.db.models import Q


class IvaListView(PermissionMixin, ListViewMixin, ListView):
  model = Iva
  template_name = 'core/ivas/list.html'
  context_object_name = 'iva'
  permission_required = 'view_iva'

  def get_queryset(self):
    q1 = self.request.GET.get('q')
    if q1:
      query = Q(description__icontains=q1)
    else:
      query = Q(active=True)

    return self.model.objects.filter(query).order_by('id')


class IvaCreateView(PermissionMixin, CreateViewMixin, CreateView):
  model = Iva
  form_class = IvaForm
  template_name = 'core/ivas/form.html'
  success_url = reverse_lazy('core:iva_list')
  permission_required = 'add_iva'

  def form_valid(self, form):
    response = super().form_valid(form)
    iva = self.object
    messages.success(self.request, f"Éxito al crear la Iva {iva.description}.")
    return response


class IvaUpdateView(PermissionMixin, UpdateViewMixin, UpdateView):
  model = Iva
  form_class = IvaForm
  template_name = 'core/ivas/form.html'
  success_url = reverse_lazy('core:iva_list')
  permission_required = 'change_iva'

  def form_valid(self, form):
    response = super().form_valid(form)
    iva = self.object
    messages.success(self.request, f"Éxito al actualizar la marca {iva.description}.")
    return response


class IvaDeleteView(PermissionMixin, DeleteViewMixin, DeleteView):
  model = Iva
  template_name = 'core/delete.html'
  success_url = reverse_lazy('core:iva_list')
  permission_required = 'delete_iva'

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.object = None

  def delete(self, request, *args, **kwargs):
    self.object = self.get_object()
    success_message = f"Éxito al eliminar el Iva {self.object.description}."
    self.object.delete()
    messages.success(self.request, success_message)
    return super().delete(request, *args, **kwargs)
