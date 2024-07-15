from django.forms import ModelForm, Select, TextInput, CheckboxInput, DateTimeInput, Textarea, SelectMultiple
from app.core.models import ProductPrice
from django import forms
from django.utils import timezone


class ProductPriceForm(ModelForm):
  class Meta:
    model = ProductPrice
    fields = ['line', 'category', 'product', 'type_increment', 'value', 'issue_date', 'observaciones', 'active']
    labels = {
      'line': 'Línea',
      'category': 'Categoría',
      'product': 'Producto Precio',
      'type_increment': 'Tipo de Aumento',
      'value': 'Incremento',
      'issue_date': 'Fecha Emisión',
      'observaciones': 'Observaciones',
      'active': 'Activo',
    }
    widgets = {
      'line': Select(attrs={
        "id": "id_line",
        "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
      }),
      'category': SelectMultiple(attrs={
        "id": "id_category",
        "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
      }),
      'product': Select(attrs={
        "id": "id_product",
        "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
      }),
      'type_increment': Select(attrs={
        "id": "id_type_increment",
        "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
      }),
      'value': TextInput(attrs={
        "placeholder": "Ingrese el incremento",
        "id": "id_value",
        "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
      }),
      'issue_date': DateTimeInput(attrs={
        "type": "datetime-local",
        "id": "id_issue_date",
        "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
      }),
      'observaciones': Textarea(attrs={
        "placeholder": "Ingrese observaciones",
        "id": "id_observaciones",
        "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
      }),
      'active': CheckboxInput(attrs={
        "id": "id_active",
        "class": "mt-1 block px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm",
      }),
    }

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    if not self.instance.pk:  # Solo establecer el valor predeterminado si el objeto es nuevo
      self.fields['issue_date'].initial = timezone.now()

  def clean_value(self):
    value = self.cleaned_data.get("value")
    if value < 0:
      raise forms.ValidationError("El incremento no puede ser negativo.")
    return value
