from app.security.mixins.mixins import CreateViewMixin, DeleteViewMixin, ListViewMixin, PermissionMixin, UpdateViewMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from app.core.forms.company import CompanyForm
from app.core.models import Company
from django.contrib import messages
from django.urls import reverse_lazy
from django.db.models import Q


class CompanyListView(PermissionMixin, ListViewMixin, ListView):
  model = Company
  template_name = 'core/company/list.html'
  context_object_name = 'company'
  permission_required = 'view_company'

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

  def form_valid(self, form):
    response = super().form_valid(form)
    company = self.object
    messages.success(self.request, f"Éxito al crear la compañía {company.name}.")
    return response


class CompanyUpdateView(PermissionMixin, UpdateViewMixin, UpdateView):
  model = Company
  form_class = CompanyForm
  template_name = 'core/company/form.html'
  success_url = reverse_lazy('core:company_list')
  permission_required = 'change_company'

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
