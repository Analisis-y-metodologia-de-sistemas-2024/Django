**Creación de tu primer proyecto Django**

Después de haber instalado y configurado el entorno de desarrollo, así como entender la estructura general de un proyecto Django, es hora de crear nuestro primer proyecto web con este maravilloso framework.

### Paso 1: Crear un nuevo proyecto Django

Para crear un nuevo proyecto Django, podemos utilizar la herramienta `django-admin` que viene incluida en el paquete oficial de Django. Abre una terminal y ejecuta el siguiente comando:
```python
django-admin startproject mi_primer_proyecto
```
Este comando creará un directorio llamado `mi_primer_proyecto` con la estructura básica para un proyecto Django.

### Paso 2: Entrar al directorio del proyecto

Una vez creado el proyecto, entra en el directorio mediante el comando:
```bash
cd mi_primer_proyecto
```
Este comando te permitirá acceder a la raíz del directorio del proyecto.

### Paso 3: Configurar el archivo `settings.py`

El archivo `settings.py` es donde se configuran las opciones básicas de nuestro proyecto, como la base de datos, los dominios y los paths. Abre el archivo en un editor de texto y modifica las siguientes líneas:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

SECRET_KEY = 'Ingrese_su_clave_secreta_aqui'

ALLOWED_HOSTS = ['*']
```
Ajusta la configuración según sea necesario para tu proyecto.

### Paso 4: Crear una aplicación

En Django, las aplicaciones son los componentes que componen nuestro proyecto. Para crear una nueva aplicación, ejecuta el siguiente comando:
```python
python manage.py startapp mi_app
```
Este comando creará un directorio llamado `mi_app` con la estructura básica para una aplicación.

### Paso 5: Modificar el archivo `settings.py`

Agrega la aplicación recién creada a la lista de aplicaciones en el archivo `settings.py`. Agrega la siguiente línea al final del archivo:
```python
INSTALLED_APPS = [
    # ...
    'mi_app',
]
```
### Paso 6: Crear una vista

Una vista es un objeto que se encarga de manejar las solicitudes HTTP y devolver respuestas. Para crear una vista, crea un nuevo archivo llamado `views.py` en la aplicación `mi_app`. Agrega el siguiente código:
```python
from django.http import HttpResponse

def saludar(request):
    return HttpResponse('¡Hola mundo!')
```
Esta vista devuelve una respuesta con el texto "¡Hola mundo!" cuando se recibe una solicitud HTTP.

### Paso 7: Crear un URL pattern

Los URL patterns son los que se encargan de mapear las solicitudes HTTP con las vistas correspondientes. Crea un nuevo archivo llamado `urls.py` en la aplicación `mi_app`. Agrega el siguiente código:
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.saludar, name='saludar'),
]
```
Este URL pattern asigna la ruta vacía (`''`) a la vista `saludar`.

### Paso 8: Crear un archivo de templates

Los archivos de templates son los que se encargan de generar la salida HTML para nuestras páginas web. Crea un nuevo directorio llamado `templates` en la aplicación `mi_app`. Dentro del directorio, crea un archivo llamado `saludar.html` con el siguiente contenido:
```html
<!DOCTYPE html>
<html>
<head>
    <title>Saludo</title>
</head>
<body>
    <h1>{{ saludar }}</h1>
</body>
</html>
```
Este archivo de template utiliza una variable llamada `saludar` para mostrar un título.

### Paso 9: Crear un enlace a la vista

Finalmente, crea un enlace a la vista en el archivo `templates/base.html` (si no existe, crea uno nuevo). Agrega el siguiente código:
```html
<a href="{% url 'saludar' %}">Saludo</a>
```
Este enlace utiliza el URL pattern definido anteriormente para acceder a la vista `saludar`.

### Paso 10: Correr el proyecto

Para correr el proyecto, ejecuta el siguiente comando:
```bash
python manage.py runserver
```
Este comando iniciará un servidor web que escuchará solicitudes en el puerto 8000 por defecto. Abre un navegador y accede a la dirección `http://localhost:8000/` para ver el resultado.

¡Eso es todo! Has creado tu primer proyecto Django. En el siguiente capítulo, aprenderás cómo trabajar con modelos y bases de datos en Django.