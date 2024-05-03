import random
import string

def generar_contrasena(longitud):
  """Genera una contraseña segura con los parámetros especificados."""

  # Lista de caracteres permitidos
  caracteres = string.ascii_letters + string.digits + string.punctuation[2:7]

  # Generar una contraseña aleatoria
  contrasena = "".join(random.choice(caracteres) for _ in range(longitud))

  # Validar la contraseña
  while not es_contrasena_valida(contrasena):
    contrasena = "".join(random.choice(caracteres) for _ in range(longitud))

  return contrasena

def es_contrasena_valida(contrasena):
  """Valida si una contraseña cumple con los requisitos especificados."""

  # Valida la longitud
  if len(contrasena) != 8:
    return False

  # Valida que no comience con mayúscula
  if contrasena[0].isupper():
    return False

  # Valida que no termine con número
  if contrasena[-1].isdigit():
    return False

  # Valida que no inicie con "="
  if contrasena[0] == "=":
    return False

  # Valida que no se repita ningún caracter
  if len(set(contrasena)) != len(contrasena):
    return False

  # Valida que no haya secuencias lógicas
  for i in range(len(contrasena) - 2):
    if contrasena[i:i+3].isdigit() or contrasena[i:i+3].isalpha():
      return False

  return True

# Generar 10 contraseñas
for i in range(10):
  contrasena = generar_contrasena(8)
  print(contrasena)