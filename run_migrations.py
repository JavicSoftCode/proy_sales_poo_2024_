# import subprocess
#
#
# def run_command(command):
#   try:
#     result = subprocess.run(command, check=True, text=True, capture_output=True)
#     print(result.stdout)
#     return True
#   except subprocess.CalledProcessError as e:
#     print(f"Error ejecutando '{' '.join(command)}': {e.stderr}")
#     return False
#
#
# def main():
#   print("\n\033[1;4;37m🔱 Aplicando... Comando Makemigrations.\033[0m\n")
#   if run_command(['python', 'manage.py', 'makemigrations']):
#     print("\033[1;32m✅  Makemigrations Completado. 🔱 \n\033[0m")
#     print("\033[1;4;37m⚜️  Aplicando... Comando Migrate\033[0m")
#     if run_command(['python', 'manage.py', 'migrate']):
#       print("\033[1;32m✅  Migraciones completadas. ⚜️\033[0m")
#     else:
#       print("\033[91m❌  Error: No se pudo aplicar el migrate.\033[0m")
#   else:
#     print("\033[91m❌  Error: No se pudo aplicar el makemigrations.\033[0m")
#
#
# if __name__ == "__main__":
#   main()
