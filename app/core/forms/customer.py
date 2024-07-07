from django.forms import ModelForm, ImageField, FileInput
from app.core.models import Customer
from django.utils import timezone
from django import forms
import datetime


class CustomerForm(ModelForm):
  dni = forms.CharField(max_length=13, label="DNI", widget=forms.TextInput(
    attrs={
      "placeholder": "Ingrese dirección",
      "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
    }
  ))
  first_name = forms.CharField(max_length=50, label="Nombres", widget=forms.TextInput(
    attrs={
      "placeholder": "Ingrese dirección",
      "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
    }
  ))
  last_name = forms.CharField(max_length=50, label="Apellidos", widget=forms.TextInput(
    attrs={
      "placeholder": "Ingrese dirección",
      "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
    }
  ))
  address = forms.CharField(max_length=255, required=False, label="Dirección", widget=forms.TextInput(
    attrs={
      "placeholder": "Ingrese dirección",
      "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
    }
  ))
  gender = forms.ChoiceField(choices=(('M', 'Masculino'), ('F', 'Femenino')), label="Sexo", widget=forms.Select(
    attrs={
      "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
    }
  ))
  date_of_birth = forms.DateField(label="Fecha de Nacimiento", required=False, widget=forms.DateInput(
    attrs={
      "type": "date",
      "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
    }
  ))
  phone = forms.CharField(max_length=50, required=False, label="Teléfono", widget=forms.TextInput(
    attrs={
      "placeholder": "Ingrese dirección",
      "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
    }
  ))
  email = forms.EmailField(required=False, label="Correo electrónico", widget=forms.TextInput(
    attrs={
      "placeholder": "Ingrese dirección",
      "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
    }
  ))
  latitude = forms.CharField(max_length=100, label="Latitud", widget=forms.TextInput(
    attrs={
      "placeholder": "Ingrese latitud",
      "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
    }
  ))
  longitude = forms.CharField(max_length=100, label="Longitud", widget=forms.TextInput(
    attrs={
      "placeholder": "Ingrese longitud",
      "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
    }
  ))
  image = forms.ImageField(required=False, label="Foto de perfil", widget=FileInput(attrs={
    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
  }))
  # active = forms.BooleanField(required=False, label="Activo", widget=forms.CheckboxInput(
  #   attrs={
  #     "class": "mt-1 block px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm",
  #   }
  # ))

  class Meta:
    model = Customer
    fields = ["dni", "first_name", "last_name", "address", "gender", "date_of_birth", "phone", "email", "latitude",
              "longitude", "image", "active"]
    error_messages = {
      "dni": {
        "unique": "Ya existe un cliente con este DNI.",
      },
      "email": {
        "unique": "Ya existe un cliente con este correo electrónico.",
      },
    }
    widgets = {
      "active": forms.CheckboxInput(
        attrs={
          "id": "id_active",
          "class": "mt-1 block px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm",
        }
      ),
    }

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

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    if not self.instance.pk:
      self.fields["date_of_birth"].initial = (timezone.now() + datetime.timedelta(days=30)).date().isoformat()

  def clean_first_name(self):
    first_name = self.cleaned_data.get("first_name")
    return first_name.upper() if first_name else first_name

  def clean_last_name(self):
    last_name = self.cleaned_data.get("last_name")
    return last_name.upper() if last_name else last_name
