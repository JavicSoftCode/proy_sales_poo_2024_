from app.core.views import brand, category, company, customer, iva, line, supplier, product, paymentMethod, price, \
  statistics
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.urls import path

app_name = 'core'
urlpatterns = [

                # URLs de marcas
                path('brands_list/', brand.BrandListView.as_view(), name='brand_list'),
                path('brands_create/', brand.BrandCreateView.as_view(), name='brand_create'),
                path('brands_update/<int:pk>/', brand.BrandUpdateView.as_view(), name='brand_update'),
                path('brands_delete/<int:pk>/', brand.BrandDeleteView.as_view(), name='brand_delete'),
                path('brand-suggestions/', brand.BrandSuggestionsView.as_view(), name='brand_suggestions'),

                # URLs de categorías
                path('category_list/', category.CategoryListView.as_view(), name='category_list'),
                path('category_create/', category.CategoryCreateView.as_view(), name='category_create'),
                path('category_update/<int:pk>/', category.CategoryUpdateView.as_view(), name='category_update'),
                path('category_delete/<int:pk>/', category.CategoryDeleteView.as_view(), name='category_delete'),
                path('category-suggestions/', category.CategorySuggestionsView.as_view(), name='category_suggestions'),

                # URLs de empresa
                path('company_list/', company.CompanyListView.as_view(), name='company_list'),
                path('company_create/', company.CompanyCreateView.as_view(), name='company_create'),
                path('company_update/<int:pk>/', company.CompanyUpdateView.as_view(), name='company_update'),
                path('company_delete/<int:pk>/', company.CompanyDeleteView.as_view(), name='company_delete'),
                path('company-suggestions/', company.CompanySuggestionsView.as_view(), name='company_suggestions'),

                # URLs de clientes
                path('customer_list/', customer.CustomerListView.as_view(), name='customer_list'),
                path('customer_create/', customer.CustomerCreateView.as_view(), name='customer_create'),
                path('customer_update/<int:pk>/', customer.CustomerUpdateView.as_view(), name='customer_update'),
                path('customer_delete/<int:pk>/', customer.CustomerDeleteView.as_view(), name='customer_delete'),
                path('customer-suggestions/', customer.CustomerSuggestionsView.as_view(), name='customer_suggestions'),

                # URLs de iva
                path('iva_list/', iva.IvaListView.as_view(), name='iva_list'),
                path('iva_create/', iva.IvaCreateView.as_view(), name='iva_create'),
                path('iva_update/<int:pk>/', iva.IvaUpdateView.as_view(), name='iva_update'),
                path('iva_delete/<int:pk>/', iva.IvaDeleteView.as_view(), name='iva_delete'),
                path('iva-suggestions/', iva.IvaSuggestionsView.as_view(), name='iva_suggestions'),

                # URLs de línea
                path('lines_list/', line.LineListView.as_view(), name='line_list'),
                path('lines_create/', line.LineCreateView.as_view(), name='line_create'),
                path('lines_update/<int:pk>/', line.LineUpdateView.as_view(), name='line_update'),
                path('lines_delete/<int:pk>/', line.LineDeleteView.as_view(), name='line_delete'),
                path('lines-suggestions/', line.LineSuggestionsView.as_view(), name='line_suggestions'),

                # URLs de metodo de pago
                path('paymentMethod_list/', paymentMethod.PaymentMethodListView.as_view(), name='paymentMethod_list'),
                path('paymentMethod_create/', paymentMethod.PaymentMethodCreateView.as_view(),
                     name='paymentMethod_create'),
                path('paymentMethod_update/<int:pk>/', paymentMethod.PaymentMethodUpdateView.as_view(),
                     name='paymentMethod_update'),
                path('paymentMethod_delete/<int:pk>/', paymentMethod.PaymentMethodDeleteView.as_view(),
                     name='paymentMethod_delete'),
                path('paymentMethod-suggestions/', paymentMethod.PaymentMethodSuggestionsView.as_view(),
                     name='paymentMethod_suggestions'),

                # URLS de precios
                path("price_list/", price.ProductPriceListView.as_view(), name="price_list"),
                path("price_create/", price.ProductPriceCreateView.as_view(), name="price_create"),
                path("price_update/<int:pk>/", price.ProductPriceUpdateView.as_view(), name="price_update"),
                path("price_delete/<int:pk>/", price.ProductPriceDeleteView.as_view(), name="price_delete"),
                path('price-suggestions/', price.ProductPriceSuggestionsView.as_view(), name='price_suggestions'),

                # URLs de productos
                path('product_list/', product.ProductListView.as_view(), name='product_list'),
                path('product_create/', product.ProductCreateView.as_view(), name='product_create'),
                path('product_update/<int:pk>/', product.ProductUpdateView.as_view(), name='product_update'),
                path('product_delete/<int:pk>/', product.ProductDeleteView.as_view(), name='product_delete'),
                path('product-suggestions/', product.ProductSuggestionsView.as_view(), name='product_suggestions'),

                # URLs de proveedores
                path('supplier_list/', supplier.SupplierListView.as_view(), name='supplier_list'),
                path('supplier_create/', supplier.SupplierCreateView.as_view(), name='supplier_create'),
                path('supplier_update/<int:pk>/', supplier.SupplierUpdateView.as_view(), name='supplier_update'),
                path('supplier_delete/<int:pk>/', supplier.SupplierDeleteView.as_view(), name='supplier_delete'),
                path('supplier-suggestions/', supplier.SupplierSuggestionsView.as_view(), name='supplier_suggestions'),

                # URLs de estadisticas
                path('sales_data/', statistics.sales_data, name='sales_data'),
                path('purchases_data/', statistics.purchases_data, name='purchases_data'),
                path('statistics_list/', statistics.StatisticsListView.as_view(), name='statistics'),
                path('invoice_details/', statistics.invoice_details, name='invoice_details'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
