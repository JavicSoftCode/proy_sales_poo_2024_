import json
from decimal import Decimal
from django.http import JsonResponse
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import View
from app.core.models import Product, Supplier, PaymentMethod


class StatisticsListView(PermissionRequiredMixin, View):
    permission_required = 'view_statistics'

    def get(self, request, *args, **kwargs):
        products = list(Product.objects.values('description', 'price', 'stock'))
        suppliers = list(Supplier.objects.values('name', 'phone'))
        payment_methods = list(PaymentMethod.objects.values('description'))

        # Convertir Decimal a float
        for product in products:
            product['price'] = float(product['price'])

        # Retornar datos en formato JSON
        data = {
            'products': products,
            'suppliers': suppliers,
            'payment_methods': payment_methods
        }
        return JsonResponse(data)
