from django.forms import ModelForm, ImageField, FileInput
from app.core.models import Company
from django import forms


class CompanyForm(ModelForm):
  dni = forms.CharField(
    max_length=13,
    label="RUC",
    widget=forms.TextInput(
      attrs={
        "placeholder": "Ingrese RUC",
        "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
      }
    )
  )
  name = forms.CharField(
    max_length=50,
    label="Empresa",
    widget=forms.TextInput(
      attrs={
        "placeholder": "Ingrese nombre de la empresa",
        "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
      }
    )
  )
  address = forms.CharField(
    max_length=200,
    required=False,
    label="Dirección",
    widget=forms.TextInput(
      attrs={
        "placeholder": "Ingrese dirección",
        "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
      }
    )
  )
  representative = forms.CharField(
    max_length=50,
    required=False,
    label="Responsable",
    widget=forms.TextInput(
      attrs={
        "placeholder": "Ingrese nombre del responsable",
        "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
      }
    )
  )
  landline = forms.CharField(
    max_length=10,
    required=False,
    label="Teléfono Fijo",
    widget=forms.TextInput(
      attrs={
        "placeholder": "Ingrese teléfono fijo",
        "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
      }
    )
  )
  website = forms.URLField(
    max_length=100,
    required=False,
    label="Sitio Web",
    widget=forms.TextInput(
      attrs={
        "placeholder": "Ingrese sitio web",
        "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
      }
    )
  )
  email = forms.EmailField(
    required=False,
    label="Correo Electrónico",
    widget=forms.TextInput(
      attrs={
        "placeholder": "Ingrese correo electrónico",
        "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
      }
    )
  )
  logo = forms.ImageField(
    required=False,
    label="Logo",
    widget=FileInput(
      attrs={
        "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
      }
    )
  )
  establishment_code = forms.CharField(
    max_length=3,
    required=False,
    label="Código de Establecimiento",
    initial='001',
    widget=forms.TextInput(
      attrs={
        "placeholder": "Ingrese código de establecimiento",
        "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
      }
    )
  )
  emission_point_code = forms.CharField(
    max_length=3,
    required=False,
    label="Código de Punto de Emisión",
    initial='001',
    widget=forms.TextInput(
      attrs={
        "placeholder": "Ingrese código de punto de emisión",
        "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
      }
    )
  )
  authorization_number = forms.CharField(
    max_length=49,
    required=False,
    label="Número de Autorización",
    widget=forms.TextInput(
      attrs={
        "placeholder": "Ingrese número de autorización",
        "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
      }
    )
  )
  taxpayer_type = forms.ChoiceField(
    choices=[
      ('special', 'Contribuyente Especial'),
      ('ordinary', 'Contribuyente Ordinario')
    ],
    label="Tipo de Contribuyente",
    initial='ordinary',
    widget=forms.Select(
      attrs={
        "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
      }
    )
  )
  # required_to_keep_accounting = forms.BooleanField(
  #   label="Obligado a Llevar Contabilidad",
  #   required=False,
  #   widget=forms.CheckboxInput(
  #     attrs={
  #       "class": "mt-1 block px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm",
  #     }
  #   )
  # )
  economic_activity_code = forms.CharField(
    max_length=10,
    required=False,
    label="Código de Actividad Económica",
    initial='1234567890',
    widget=forms.TextInput(
      attrs={
        "placeholder": "Ingrese código de actividad económica",
        "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
      }
    )
  )
  widgets = {
    "required_to_keep_accounting": forms.CheckboxInput(
      attrs={
        "id": "id_required_to_keep_accounting",
        "class": "mt-1 block px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm",
      }
    ),
  }

  class Meta:
    model = Company
    fields = ["dni", "name", "address", "representative", "landline", "website", "email", "logo",
              "establishment_code", "emission_point_code", "authorization_number", "taxpayer_type",
              "required_to_keep_accounting", "economic_activity_code"]
    labels = {
      "dni": "RUC",
      "name": "Empresa",
      "address": "Dirección",
      "representative": "Responsable",
      "landline": "Teléfono Fijo",
      "website": "Sitio Web",
      "email": "Correo Electrónico",
      "logo": "Logo",
      "establishment_code": "Código de Establecimiento",
      "emission_point_code": "Código de Punto de Emisión",
      "authorization_number": "Número de Autorización",
      "taxpayer_type": "Tipo de Contribuyente",
      "required_to_keep_accounting": "Obligado a Llevar Contabilidad",
      "economic_activity_code": "Código de Actividad Económica"
    }
