from django.forms import ModelForm, ImageField, FileInput
from app.core.models import Company
from django import forms


class CompanyForm(ModelForm):
  logo = forms.ImageField(required=False, label="Logo", widget=FileInput(attrs={
    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
  }))

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
    error_messages = {
      "dni": {
        "unique": "Ya existe una compañía con este RUC.",
      },
<<<<<<< HEAD
      "name": {
        "unique": "Ya existe una compañía con este nombre.",
      },
      "email": {
        "unique": "Ya existe una compañía con este correo electrónico.",
      },
      "website": {
        "unique": "Ya existe una compañía con este sitio web.",
      },
      "landline": {
        "unique": "Ya existe una compañía con este teléfono fijo.",
      },
      "establishment_code": {
        "unique": "Ya existe un código de establecimiento.",
      },
    }

=======
    }
>>>>>>> 748233b376cadbaee22ab464bb0b0ac354bcffa6
    widgets = {
      "dni": forms.TextInput(attrs={
        "placeholder": "Ingrese RUC",
        "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
      }),
      "name": forms.TextInput(attrs={
        "placeholder": "Ingrese nombre de la empresa",
        "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
      }),
      "address": forms.TextInput(attrs={
        "placeholder": "Ingrese dirección",
        "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
      }),
      "representative": forms.TextInput(attrs={
        "placeholder": "Ingrese nombre del responsable",
        "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
      }),
      "landline": forms.TextInput(attrs={
        "placeholder": "Ingrese teléfono fijo",
        "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
      }),
      "website": forms.URLInput(attrs={
        "placeholder": "Ingrese sitio web",
        "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
      }),
      "email": forms.EmailInput(attrs={
        "placeholder": "Ingrese correo electrónico",
        "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
      }),
      "establishment_code": forms.TextInput(attrs={
        "placeholder": "Ingrese código de establecimiento",
        "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
      }),
      "emission_point_code": forms.TextInput(attrs={
        "placeholder": "Ingrese código de punto de emisión",
        "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
      }),
      "authorization_number": forms.TextInput(attrs={
        "placeholder": "Ingrese número de autorización",
        "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
      }),
      "taxpayer_type": forms.Select(attrs={
        "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
      }),
      "required_to_keep_accounting": forms.CheckboxInput(attrs={
        "id": "id_required_to_keep_accounting",
        "class": "mt-1 block px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm",
      }),
      "economic_activity_code": forms.TextInput(attrs={
        "placeholder": "Ingrese código de actividad económica",
        "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
      }),
    }

  def clean_name(self):
    name = self.cleaned_data.get("name")
    return name.upper()

  def clean_address(self):
    address = self.cleaned_data.get("address")
    return address.upper()

  def clean_representative(self):
    representative = self.cleaned_data.get("representative")
    return representative.upper()

  def clean_email(self):
    email = self.cleaned_data.get("email")
    return email.lower()

  def clean_economic_activity_code(self):
    economic_activity_code = self.cleaned_data.get("economic_activity_code")
    return economic_activity_code.upper()
