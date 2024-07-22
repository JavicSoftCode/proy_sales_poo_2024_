from django.urls import path
from app.sales.views import sale

app_name = 'sales'

urlpatterns = [
  # URLs para la gestión de ventas
  path('sales_list/', sale.SaleListView.as_view(), name='sales_list'),
  path('sales_create/', sale.SaleCreateView.as_view(), name='sales_create'),
  path('sales_update/<int:pk>/', sale.SaleUpdateView.as_view(), name='sales_update'),
  path('sales/cancel/<int:pk>/', sale.SaleCancelView.as_view(), name='sales_cancel'),
  path('sales/delete/<int:pk>/', sale.SaleDeleteView.as_view(), name='sales_delete'),
  path('sales/<int:invoice_id>/pdf/', sale.generate_invoice_pdf, name='invoice_pdf'),
  path('sales/consult/<int:pk>/', sale.SalesConsultView.as_view(), name='sales_consult'),
  path('sales-suggestions/', sale.SalesSuggestionsView.as_view(), name='sales_suggestions'),

]
