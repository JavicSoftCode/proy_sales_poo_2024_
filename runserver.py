import subprocess
import sys
import time
import webbrowser
import signal
import requests

BRAVE_PATH = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"

DJANGO_COMMAND = [sys.executable, "manage.py", "runserver", "8000"]

server_process = None


def is_server_running(url="http://127.0.0.1:8000"):
  try:
    response = requests.get(url)
    return response.status_code == 200
  except requests.ConnectionError:
    return False


def start_server():
  global server_process
  server_process = subprocess.Popen(DJANGO_COMMAND, shell=False)
  print("Activando el servidor de Django...")
  while not is_server_running():
    print("Servidor de Django no disponible, reintentando en 1 segundo...")
    time.sleep(1)
  print("El servidor de Django está activo...")
  webbrowser.register('brave', None, webbrowser.BackgroundBrowser(BRAVE_PATH))
  webbrowser.get('brave').open('http://127.0.0.1:8000')
  server_process.communicate()


def stop_server(signum, frame):
  global server_process
  if server_process is not None:
    print("Apagando el servidor de Django...")
    server_process.terminate()
    server_process.wait()
    print("El servidor de Django ha sido apagado.")


if __name__ == "__main__":

  signal.signal(signal.SIGINT, stop_server)
  signal.signal(signal.SIGTERM, stop_server)

  start_server()
