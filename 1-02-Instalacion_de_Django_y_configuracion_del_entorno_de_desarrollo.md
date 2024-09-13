**Instalación de Django y Configuración del Entorno de Desarrollo**

En el capítulo anterior, exploramos los conceptos básicos de Django y su importancia en el desarrollo web. Ahora, vamos a profundizar en la instalación y configuración del entorno de desarrollo de Django.

**Requisitos previos**

Antes de empezar con la instalación de Django, es importante tener en cuenta algunos requisitos previos:

* Python: Es necesario tener instalado Python 3.x o superior. Puedes descargar la versión más reciente desde el sitio oficial de Python.
* pip: pip es el administrador de paquetes de Python y se utiliza para instalar Django. Si no tienes pip instalado, puedes hacerlo mediante el comando `python -m ensurepip`.
* Git (opcional): Si deseas trabajar con proyectos Django en colaboración, es recomendable utilizar Git como sistema de control de versiones.

**Instalación de Django**

La instalación de Django se puede realizar utilizando pip. Para instalar la versión más reciente de Django, ejecuta el comando siguiente:

```
pip install django
```

Otra forma de instalar Django es mediante el uso de virtualenv. Virtualenv es un herramienta que te permite crear entornos de desarrollo aislados y reproducibles. Primero debes instalar virtualenv utilizando pip:

```
pip install virtualenv
```

Luego, crea un nuevo directorio para tu proyecto y entra en él:

```
mkdir mi_proyecto
cd mi_proyecto
```

Finalmente, crea un entorno virtual y activa el directorio:

```
virtualenv mi_entorno
source mi_entorno/bin/activate
```

Ahora puedes instalar Django utilizando pip dentro del entorno virtual:

```
pip install django
```

**Configuración del entorno de desarrollo**

Una vez instalado Django, es hora de configurar el entorno de desarrollo. Django utiliza un archivo llamado `settings.py` para configurar el proyecto.

El archivo `settings.py` se encuentra en la raíz del directorio de tu proyecto y contiene varias opciones para personalizar el comportamiento de Django. Algunas de las opciones más importantes son:

* `INSTALLED_APPS`: Es una lista de aplicaciones que se van a utilizar en el proyecto.
* `DATABASES`: Define la configuración de la base de datos utilizada por el proyecto.
* `SECRET_KEY`: Es una cadena secreta que se utiliza para generar tokens de seguridad.
* `DEBUG`: Indica si se debe activar el modo depuración o no.

Aquí te muestro un ejemplo básico de cómo podría quedar el archivo `settings.py`:

```
import os

# Configuración general
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Configuración de la base de datos
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Configuración de aplicaciones instaladas
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# Configuración secreta
SECRET_KEY = 'mi_clave_secreta'

# Configuración de depuración
DEBUG = True

# Configuración de directors de archivos estáticos y media
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
```

**Creando un proyecto Django**

Una vez configurado el entorno de desarrollo, es hora de crear un proyecto Django. Para hacerlo, ejecuta el comando siguiente:

```
django-admin startproject mi_proyecto
```

Este comando creará una nueva carpeta llamada `mi_proyecto` con los archivos básicos para un proyecto Django.

**Estructura del proyecto**

La estructura de un proyecto Django por defecto es la siguiente:

* `mi_proyecto/`: Carpeta raíz del proyecto.
	+ `manage.py`: Archivo que se utiliza para gestionar el proyecto.
	+ `mi_proyecto/`: Carpeta que contiene los archivos de configuración y aplicaciones del proyecto.
		- `settings.py`: Archivo que contiene las configuraciones del proyecto.
		- `urls.py`: Archivo que contiene las rutas del proyecto.
		- `wsgi.py`: Archivo que se utiliza para configurar el servidor web.

**Conclusión**

En este capítulo, hemos aprendido a instalar y configurar el entorno de desarrollo de Django. También hemos creado un nuevo proyecto Django y explorado la estructura básica del mismo. En el próximo capítulo, vamos a profundizar en las aplicaciones y modelos de Django.

**Ejercicio**

1. Instala Django en una nueva carpeta llamada `mi_proyecto`.
2. Configura el archivo `settings.py` con tus propias opciones.
3. Crea un nuevo proyecto Django utilizando el comando `django-admin startproject mi_proyecto`.
4. Explora la estructura del proyecto y explica los archivos más importantes.

**Respuestas**

1. El comando para instalar Django es `pip install django`.
2. El archivo `settings.py` contiene las configuraciones del proyecto, incluyendo la lista de aplicaciones instaladas, la configuración de la base de datos y la clave secreta.
3. El comando para crear un nuevo proyecto Django es `django-admin startproject mi_proyecto`.
4. La estructura básica de un proyecto Django consta de la carpeta raíz del proyecto, el archivo `manage.py` y las carpetas `mi_proyecto/` con los archivos de configuración y aplicaciones.

Espero que hayas disfrutado este capítulo y estés listo para aprender más sobre Django. En el próximo capítulo, vamos a profundizar en las aplicaciones y modelos de Django.