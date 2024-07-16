from django.forms import ModelForm, ImageField, FileInput
from app.core.models import Iva
from django.utils import timezone
from django import forms
import datetime


class IvaForm(ModelForm):
  image = forms.ImageField(required=False, label="Foto de Iva", widget=FileInput(attrs={
    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
  }))

  class Meta:
    model = Iva
    fields = ["description", "value", "active", "image"]
    labels = {
      "description": "Descripción ",
      "value": "Porcentaje",
      "state": "Estado",
      "image": "Imagen",
    }
    error_messages = {
      "description": {
        "unique": "Ya existe un Iva con esta decripcion.",
      },
    }
    widgets = {
      "description": forms.TextInput(attrs={
        "placeholder": "Ingrese descripción del Iva",
        "id": "id_description",
        "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
      }),
      "value": forms.NumberInput(attrs={
        "placeholder": "Ingrese Porcentaje",
        "min": "0",
        "max": "15",
        "id": "id_value",
        "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
      }),
      "state": forms.CheckboxInput(attrs={
        "class": "mt-1 block px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
      }),
    }

  def clean_description(self):
    description = self.cleaned_data.get("description")
    return description.upper()
