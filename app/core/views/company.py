from app.security.mixins.mixins import CreateViewMixin, DeleteViewMixin, ListViewMixin, PermissionMixin, UpdateViewMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from app.core.forms.company import CompanyForm
from app.core.models import Company
from django.contrib import messages
from django.urls import reverse_lazy
from django.db.models import Q


class CompanyListView(PermissionMixin, ListViewMixin, ListView):
<<<<<<< HEAD
  model = Company
  template_name = 'core/company/list.html'
  context_object_name = 'company'
  permission_required = 'view_company'
=======
    model = Company
    template_name = 'core/company/list.html'
    context_object_name = 'company'
    permission_required = 'view_company'
>>>>>>> 748233b376cadbaee22ab464bb0b0ac354bcffa6

  def get_queryset(self):
    q = self.request.GET.get('q')
    queryset = self.model.objects.all().order_by('id')
    if q:
      queryset = queryset.filter(Q(dni__icontains=q) | Q(name__icontains=q))

<<<<<<< HEAD
    return queryset
=======
        if q:
          queryset = queryset.filter(Q(dni__icontains=q) | Q(name__icontains=q))

        return queryset

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     queryset = self.get_queryset()
    #
    #     paginator = Paginator(queryset, self.paginate_by)
    #
    #     page = self.request.GET.get('page')
    #     try:
    #         companies = paginator.page(page)
    #     except PageNotAnInteger:
    #         companies = paginator.page(1)
    #     except EmptyPage:
    #         companies = paginator.page(paginator.num_pages)
    #
    #     context['companies'] = companies
    #     context['title1'] = 'Compañías'
    #     context['title2'] = 'Consulta de Compañías'
    #     context['create_url'] = reverse_lazy('core:company_create')
    #     context['query'] = self.request.GET.get('q', '')
    #     return context
>>>>>>> 748233b376cadbaee22ab464bb0b0ac354bcffa6


class CompanyCreateView(PermissionMixin, CreateViewMixin, CreateView):
  model = Company
  form_class = CompanyForm
  template_name = 'core/company/form.html'
  success_url = reverse_lazy('core:company_list')
  permission_required = 'add_company'

<<<<<<< HEAD
  def form_valid(self, form):
    response = super().form_valid(form)
    company = self.object
    messages.success(self.request, f"Éxito al crear la compañía {company.name}.")
    return response
=======
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['title1'] = 'Crear Compañía'
    #     context['title2'] = 'Compañía'
    #     context['back_url'] = self.success_url
    #     return context

    def form_valid(self, form):
        response = super().form_valid(form)
        company = self.object
        messages.success(self.request, f"Éxito al crear la compañía {company.name}.")
        return response
>>>>>>> 748233b376cadbaee22ab464bb0b0ac354bcffa6


class CompanyUpdateView(PermissionMixin, UpdateViewMixin, UpdateView):
  model = Company
  form_class = CompanyForm
  template_name = 'core/company/form.html'
  success_url = reverse_lazy('core:company_list')
  permission_required = 'change_company'

<<<<<<< HEAD
  def form_valid(self, form):
    response = super().form_valid(form)
    company = self.object
    messages.success(self.request, f"Éxito al actualizar la compañía {company.name}.")
    return response
=======
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['title1'] = 'Actualizar Compañía'
    #     context['title2'] = 'Actualizar Datos de la Compañía'
    #     context['back_url'] = self.success_url
    #     return context

    def form_valid(self, form):
        response = super().form_valid(form)
        company = self.object
        messages.success(self.request, f"Éxito al actualizar la compañía {company.name}.")
        return response
>>>>>>> 748233b376cadbaee22ab464bb0b0ac354bcffa6


class CompanyDeleteView(PermissionMixin, DeleteViewMixin, DeleteView):
  model = Company
  template_name = 'core/delete.html'
  success_url = reverse_lazy('core:company_list')
  permission_required = 'delete_company'

<<<<<<< HEAD
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.object = None
=======
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['title'] = 'Eliminar Compañía'
    #     context['description'] = f"¿Desea eliminar la compañía: {self.object.name}?"
    #     context['back_url'] = self.success_url
    #     return context

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.object = None
>>>>>>> 748233b376cadbaee22ab464bb0b0ac354bcffa6

  def delete(self, request, *args, **kwargs):
    self.object = self.get_object()
    success_message = f"Éxito al eliminar la compañía {self.object.name}."
    self.object.required_to_keep_accounting = False
    self.object.save()
    messages.success(self.request, success_message)
    return super().delete(request, *args, **kwargs)
