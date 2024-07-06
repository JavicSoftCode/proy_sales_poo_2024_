from django.urls import path
from app.core.views import supplier, brand, category, product
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

app_name = 'core'  # define un espacio de nombre para la aplicación
urlpatterns = [
                # URLs de proveedores
                path('supplier_list/', supplier.SupplierListView.as_view(), name='supplier_list'),
                path('supplier_create/', supplier.SupplierCreateView.as_view(), name='supplier_create'),
                path('supplier_update/<int:pk>/', supplier.SupplierUpdateView.as_view(), name='supplier_update'),
                path('supplier_delete/<int:pk>/', supplier.SupplierDeleteView.as_view(), name='supplier_delete'),

                # URLs de marcas
                path('brands_list/', brand.BrandListView.as_view(), name='brand_list'),
                path('brands_create/', brand.BrandCreateView.as_view(), name='brand_create'),
                path('brands_update/<int:pk>/', brand.BrandUpdateView.as_view(), name='brand_update'),
                path('brands_delete/<int:pk>/', brand.BrandDeleteView.as_view(), name='brand_delete'),

                # URLs de categorías
                path('category_list/', category.CategoryListView.as_view(), name='category_list'),
                path('category_create/', category.CategoryCreateView.as_view(), name='category_create'),
                path('category_update/<int:pk>/', category.CategoryUpdateView.as_view(), name='category_update'),
                path('category_delete/<int:pk>/', category.CategoryDeleteView.as_view(), name='category_delete'),

                #     # URLs de productos
                path('product_list/', product.ProductListView.as_view(), name='product_list'),
                path('product_create/', product.ProductCreateView.as_view(), name='product_create'),
                path('product_update/<int:pk>/', product.ProductUpdateView.as_view(), name='product_update'),
                path('product_delete/<int:pk>/', product.ProductDeleteView.as_view(), name='product_delete'),

                # path('product_list/', views.product_List, name='product_list'),
                # path('product_create/', views.product_create, name='product_create'),
                # path('product_update/<int:id>/', views.product_update, name='product_update'),
                # path('product_delete/<int:id>/', views.product_delete, name='product_delete'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#     path('purchase/', include('app.purchase.urls')),
#
