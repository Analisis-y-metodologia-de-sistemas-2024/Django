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