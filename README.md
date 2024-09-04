# pre-HernanPerea

## Este es un proyecto web desarrollado con Django para gestionar una pastelería. La aplicacion permite ver, añadir y gestionar tortas, clientes, y pedidos a través de un sistema de administracion.

## ## Instalación

Clona el repositorio:

   git clone https://github.com/herrnito/pre-HernanPerea.git
   
  
Crea y activa un entorno virtual:

   python -m venv env
   source env/bin/activate  # En Linux/Mac
   .\env\Scripts\activate  # En Windows
  

Realiza las migraciones y crea un superusuario:

   python manage.py makemigrations
   python manage.py migrate
   python manage.py createsuperuser
 

Ejecuta el servidor:

    python manage.py runserver
  

Accede a la aplicación en tu navegador en `http://127.0.0.1:8000/`
 

## Uso

Accede a la página principal en `http://127.0.0.1:8000/`.
Desde ahi, podes:
  Ver la lista de tortas disponibles en `http://127.0.0.1:8000/tortas/`.
  Agregar nuevas tortas en `http://127.0.0.1:8000/torta/create/`.
  Buscar tortas en `http://127.0.0.1:8000/tortas/list/`.
  Gestionar clientes y pedidos desde las respectivas páginas.