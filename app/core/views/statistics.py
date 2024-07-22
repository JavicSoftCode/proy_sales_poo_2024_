from django.http import JsonResponse
from app.purcharse.models import Purchase
from app.sales.models import Invoice, InvoiceDetail
from app.core.models import Product
from django.views.decorators.http import require_GET
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import TemplateView
from django.db.models import Sum
from django.utils.dateparse import parse_date


@require_GET
def invoice_details(request):
    details = InvoiceDetail.objects.values(
        'product__description'
    ).annotate(total_quantity=Sum('quantity')).order_by('-total_quantity')

    products_list = [
        {
            'product_name': detail['product__description'],
            'total_quantity': detail['total_quantity']
        } for detail in details
    ]
    return JsonResponse(products_list, safe=False)


class StatisticsListView(PermissionRequiredMixin, TemplateView):
  template_name = 'core/statistics/graphicStatistics.html'
  permission_required = 'view_statistics'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['title1'] = "Estadísticas"
    context['title2'] = 'Gráficas Estadísticas'
    return context


@require_GET
def sales_data(request):
  invoices = Invoice.objects.all().values(
    'id',
    'customer__dni',
    'customer__first_name',
    'customer__last_name',
    'issue_date',
    'total',
    'state',
    'active'
  )
  invoices_list = [
    {
      'id': sale['id'],
      'customer_dni': sale['customer__dni'],
      'customer': sale['customer__first_name'],
      'customer_last': sale['customer__last_name'],
      'issue_date': sale['issue_date'],
      'total': sale['total'],
      'state': sale['state'],
      'active': sale['active']
    } for sale in invoices
  ]
  return JsonResponse(invoices_list, safe=False)


@require_GET
def purchases_data(request):
  purchases = Purchase.objects.all().values(
    'id',
    'supplier__ruc',
    'supplier__name',
    'issue_date',
    'total',
    'state',
    'active'
  )
  purchases_list = [
    {
      'id': purchase['id'],
      'supplier_ruc': purchase['supplier__ruc'],
      'supplier_name': purchase['supplier__name'],
      'issue_date': purchase['issue_date'],
      'total': purchase['total'],
      'state': purchase['state'],
      'active': purchase['active']
    } for purchase in purchases
  ]
  return JsonResponse(purchases_list, safe=False)
