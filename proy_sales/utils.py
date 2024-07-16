from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from app.security.models import AuditUser
from django.utils import timezone
import random
import string
from django.utils.translation import gettext_lazy as _
from datetime import date
import datetime


def get_current_datetime(value):
  current_date = timezone.now().date()
  if value.date() != current_date:
    raise ValidationError('La fecha de emisión debe ser el día actual.')


def validate_expiration_date(value):
    # Esta función valida si la fecha de expiración proporcionada es válida
    if value <= timezone.now():
        raise ValidationError(_('La fecha de caducidad no puede ser en el pasado. Debe ser una fecha futura.'))


def validate_date_of_birth(value):
  # Esta función valida si la fecha de nacimiento proporcionada es válida
  if value:
    if value > date.today():
      raise ValidationError(_('La fecha de nacimiento no puede ser en el futuro.'))
    elif value.year < 1940:
      raise ValidationError(
        _('Error: Esta persona probablemente está fallecida ☠☠☠.'))


phone_regex = RegexValidator(
  # Expresión regular que define el patrón permitido para el número de teléfono
  regex=r'^(\+\d{1,3}\s?)?\d{9,12}$',
  # Mensaje de error que se mostrará si el número de teléfono no cumple con el patrón especificado
  message="El número de teléfono debe contener entre 9 y 15 dígitos, con un código de país opcional en formato '+XXX '."
)

ecuador_landline_regex = RegexValidator(
  regex=r'^\(0[2-7]\) \d{4}-\d{4}$',
  message="Formato correcto: (0X) XXXX-XXXX, donde 0X es el código de área."
  # (por ejemplo, 02 para Quito, 04 para Guayaquil)
)


def generate_random_authorization_number():
  # Longitud del número de autorización
  length = 49
  # Caracteres permitidos para el número de autorización
  characters = string.digits
  # Genera el número aleatorio utilizando caracteres aleatorios
  return ''.join(random.choices(characters, k=length))


def generate_establishment_code(code=None):
  # Generar un código aleatorio de tres dígitos entre 001 y 999
  return f'{random.randint(1, 999):03}'


def valida_ruc(value):
  ruc = str(value)

  if not ruc.isdigit():
    raise ValidationError('El RUC debe contener solo números.')

  if len(ruc) != 13:
    raise ValidationError('El RUC debe tener 13 dígitos.')

  coeficientes = [2, 1, 2, 1, 2, 1, 2, 1, 2]

  total = 0

  for i in range(9):
    digito = int(ruc[i])

    coeficiente = coeficientes[i]

    producto = digito * coeficiente

    if producto > 9:
      producto -= 9

    total += producto

  digito_verificador = (total * 9) % 10

  if digito_verificador != int(ruc[9]):
    raise ValidationError('El RUC no es válido.')


def valida_cedula(value):
  cedula = str(value)
  if not cedula.isdigit():
    raise ValidationError('La cédula debe contener solo números.')

  longitud = len(cedula)
  if longitud != 10:
    raise ValidationError('Cantidad de dígitos incorrecta.')

  coeficientes = [2, 1, 2, 1, 2, 1, 2, 1, 2]
  total = 0
  for i in range(9):
    digito = int(cedula[i])
    coeficiente = coeficientes[i]
    producto = digito * coeficiente
    if producto > 9:
      producto -= 9
    total += producto

  digito_verificador = (total * 9) % 10
  if digito_verificador != int(cedula[9]):
    raise ValidationError('La cédula no es válida.')


def valida_numero_entero_positivo(value):
  if not str(value).isdigit() or int(value) <= 0:
    raise ValidationError('Debe ingresar un número entero positivo válido.')


def valida_numero_flotante_positivo(value):
  try:
    valor_float = float(value)
    if valor_float <= 0:
      raise ValidationError('Debe ingresar un número flotante positivo válido.')
  except ValueError:
    raise ValidationError('Debe ingresar un número flotante válido.')


# class Parameters:
#     LOGO_SYSTEM = '/static/img/iguana_corporation.png'
#     SYSTEM_NAME = 'E-ComPro'

#     # ACTIONS FOR AUDIT TABLES
#     ACTION_ADD = 'A'
#     ACTION_MODIFY = 'M'
#     ACTION_DELETE = 'E'


def save_audit(request, model, action):
  user = request.user

  # Obtain client ip address
  client_address = ip_client_address(request)

  # Registro en tabla Auditora BD
  auditusuariotabla = AuditUser(usuario=user,
                                tabla=model.__class__.__name__,
                                registroid=model.id,
                                accion=action,
                                fecha=timezone.now().date(),
                                hora=timezone.now().time(),
                                estacion=client_address)
  auditusuariotabla.save()


# Obtener el IP desde donde se esta accediendo
def ip_client_address(request):
  try:
    # case server externo
    client_address = request.META['HTTP_X_FORWARDED_FOR']
  except:
    # case localhost o 127.0.0.1
    client_address = request.META['REMOTE_ADDR']

  return client_address
