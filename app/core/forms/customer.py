from django.forms import ModelForm, ImageField, FileInput
from app.core.models import Customer
from django.utils import timezone
from django import forms
import datetime


class CustomerForm(ModelForm):
  image = forms.ImageField(required=False, label="Foto de perfil", widget=FileInput(attrs={
    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
  })),

  class Meta:
    model = Customer
    fields = ["dni", "first_name", "last_name", "address", "gender", "date_of_birth", "phone", "email", "latitude",
              "longitude", "image", "active"]
    labels = {
      "dni": "DNI",
      "first_name": "Nombres",
      "last_name": "Apellidos",
      "address": "Dirección",
      "gender": "Sexo",
      "date_of_birth": "Fecha de Nacimiento",
      "phone": "Teléfono",
      "email": "Correo electrónico",
      "latitude": "Latitud",
      "longitude": "Longitud",
      "image": "Foto de perfil",
      "active": "Activo",
    }
    error_messages = {
      "dni": {
        "unique": "Ya existe un cliente con este DNI.",
      },
      "email": {
        "unique": "Ya existe un cliente con este correo electrónico.",
      },
      "phone": {
        "unique": "Ya existe un cliente con este correo electrónico.",
      },
    }
    widgets = {
      "dni": forms.TextInput(attrs={
        "placeholder": "Ingrese DNI",
        "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
      }),
      "date_of_birth": forms.DateInput(attrs={
        'type': 'date',
        'class': 'shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light',
      }),
      "first_name": forms.TextInput(attrs={
        "placeholder": "Ingrese nombres",
        "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
      }),
      "last_name": forms.TextInput(attrs={
        "placeholder": "Ingrese apellidos",
        "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
      }),
      "address": forms.TextInput(attrs={
        "placeholder": "Ingrese dirección",
        "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
      }),
      "gender": forms.Select(choices=(('M', 'Masculino'), ('F', 'Femenino')), attrs={
        "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
      }),
      "phone": forms.TextInput(attrs={
        "placeholder": "Ingrese teléfono",
        "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
      }),
      "email": forms.EmailInput(attrs={
        "placeholder": "Ingrese correo electrónico",
        "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
      }),
      "latitude": forms.TextInput(attrs={
        "placeholder": "Ingrese latitud",
        "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
      }),
      "longitude": forms.TextInput(attrs={
        "placeholder": "Ingrese longitud",
        "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
      }),
      "active": forms.CheckboxInput(attrs={
        "id": "id_active",
        "class": "mt-1 block px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm",
      }),
    }

  def clean_first_name(self):
    first_name = self.cleaned_data.get("first_name")
    return first_name.upper() if first_name else first_name

  def clean_last_name(self):
    last_name = self.cleaned_data.get("last_name")
    return last_name.upper() if last_name else last_name
