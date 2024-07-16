<<<<<<< HEAD
from app.security.mixins.mixins import CreateViewMixin, DeleteViewMixin, ListViewMixin, PermissionMixin, UpdateViewMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from app.core.forms.line import LineForm
from app.core.models import Line
from django.contrib import messages
from django.urls import reverse_lazy
=======
from django.urls import reverse_lazy
from app.core.forms.line import LineForm
from app.core.models import Line
from app.security.instance.menu_module import MenuModule
from app.security.mixins.mixins import CreateViewMixin, DeleteViewMixin, ListViewMixin, PermissionMixin, UpdateViewMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib import messages
>>>>>>> 748233b376cadbaee22ab464bb0b0ac354bcffa6
from django.db.models import Q


class LineListView(PermissionMixin, ListViewMixin, ListView):
  model = Line
  template_name = 'core/line/list.html'
  context_object_name = 'lines'
<<<<<<< HEAD
  permission_required = 'view_line'
=======
  permission_required = 'view_lines'
>>>>>>> 748233b376cadbaee22ab464bb0b0ac354bcffa6

  def get_queryset(self):
    q1 = self.request.GET.get('q')
    if q1:
      query = Q(description__icontains=q1)
    else:
      query = Q(active=True)

    return self.model.objects.filter(query).order_by('id')


class LineCreateView(PermissionMixin, CreateViewMixin, CreateView):
  model = Line
  form_class = LineForm
  template_name = 'core/line/form.html'
  success_url = reverse_lazy('core:line_list')
<<<<<<< HEAD
  permission_required = 'add_line'
=======
  permission_required = 'add_lines'
>>>>>>> 748233b376cadbaee22ab464bb0b0ac354bcffa6

  def form_valid(self, form):
    response = super().form_valid(form)
    linea = self.object
    messages.success(self.request, f"Éxito al crear la linea {linea.description}.")
    return response


class LineUpdateView(PermissionMixin, UpdateViewMixin, UpdateView):
  model = Line
  form_class = LineForm
  template_name = 'core/line/form.html'
  success_url = reverse_lazy('core:line_list')
<<<<<<< HEAD
  permission_required = 'change_line'
=======
  permission_required = 'change_lines'
>>>>>>> 748233b376cadbaee22ab464bb0b0ac354bcffa6

  def form_valid(self, form):
    response = super().form_valid(form)
    line = self.object
    messages.success(self.request, f"Éxito al actualizar la linea {line.description}.")
    return response


class LineDeleteView(PermissionMixin, DeleteViewMixin, DeleteView):
  model = Line
  template_name = 'core/delete.html'
  success_url = reverse_lazy('core:line_list')
<<<<<<< HEAD
  permission_required = 'delete_line'
=======
  permission_required = 'delete_lines'
>>>>>>> 748233b376cadbaee22ab464bb0b0ac354bcffa6

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.object = None

  def delete(self, request, *args, **kwargs):
    self.object = self.get_object()
    success_message = f"Éxito al eliminar la linea {self.object.description}."
    self.object.delete()
    messages.success(self.request, success_message)
    return super().delete(request, *args, **kwargs)
