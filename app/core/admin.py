from django.contrib import admin

from app.core.models import Supplier,Product,Brand,Line,Category,Iva,Customer,PaymentMethod

admin.site.register(Supplier)
admin.site.register(Product)
admin.site.register(Brand)
admin.site.register(Line)
admin.site.register(Category)
admin.site.register(Iva)
admin.site.register(Customer)
admin.site.register(PaymentMethod)
