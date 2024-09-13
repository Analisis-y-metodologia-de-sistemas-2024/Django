**Capítulo 8: Internacionalización y Localización**

En el mundo globalizado que vivimos, la internacionalización y localización de aplicaciones web son fundamentales para cualquier proyecto que desee alcanzar un público amplio y diverso. En este capítulo, exploraremos cómo Django nos permite hacer esto con facilidad.

**¿Por qué es importante la internacionalización y localización?**

La internacionalización (i18n) se refiere al proceso de preparar una aplicación para ser utilizada en diferentes idiomas y regiones, mientras que la localización (L10n) implica adaptar la aplicación a las específicas necesidades de un mercado o región.

Por ejemplo, si deseas que tu aplicación esté disponible en español para usuarios argentinos, pero también en inglés para usuarios estadounidenses, necesitarás internacionalizar y localizar tu aplicación. De esta manera, podrás ofrecer una experiencia más personalizada y atractiva para tus usuarios en diferentes partes del mundo.

**Configuración básica de la internacionalización**

En Django, la configuración básica de la internacionalización se realiza mediante el archivo `settings.py`. En este archivo, debes agregar las siguientes líneas:

```
USE_I18N = True
LANGUAGE_CODE = 'es-ar'  # O cualquier otro código de idioma que deseas
TIME_ZONE = 'America/Argentina/Buenos_Aires'  # O cualquier otra zona horaria que desees
```

**Creación de paquetes de traducción**

Para crear un paquete de traducción, necesitarás crear un directorio en la carpeta `locale` dentro de tu proyecto. El nombre del directorio debe ser el código de idioma seguido del guion bajo y el código de país (por ejemplo, `es_AR` para español argentino).

Dentro de este directorio, debes crear los archivos de traducción. Por defecto, Django utiliza archivos de texto en formato PO (Portable Object) como fuentes de traducción. Puedes generar estos archivos automáticamente utilizando la herramienta `makemessages`:

```
python manage.py makemessages -l es_AR
```

**Traducción de mensajes**

Para traducir los mensajes, debes editar el archivo `messages.po` y reemplazar los textos originales con las traducciones correspondientes.

Por ejemplo, si deseas traducir el mensaje "Hello, world!" al español argentino, deberías agregar la siguiente línea al archivo `messages.po`:

```
#: models.py:12
msgid "Hello, world!"
msgstr "Hola, mundo!"
```

**Compilación de archivos de traducción**

Una vez que hayas terminado de traducir los mensajes, debes compilar los archivos de traducción utilizando la herramienta `compilemessages`:

```
python manage.py compilemessages
```

**Uso de la internacionalización en el proyecto**

Para utilizar la internacionalización en tu proyecto, puedes hacerlo mediante el uso del template tag `{% trans "mensaje" %}`. Por ejemplo:

```
{% extends 'base.html' %}

{% block content %}
  <h1>{% trans "Hello, world!" %}</h1>
{% endblock %}
```

Django automáticamente buscará la traducción correspondiente en el archivo `messages.po` y reemplazará el texto original con la traducción.

**Uso de internacionalización en forms**

Para utilizar la internacionalización en formularios, puedes hacerlo mediante el uso del método `__unicode__` o `__str__`. Por ejemplo:

```
from django import forms
from django.utils.translation import gettext_lazy as _

class MyForm(forms.Form):
    name = forms.CharField(label=_('Nombre'))
    email = forms.EmailField(label=_('Correo electrónico'))

    def __unicode__(self):
        return _('formulario de contacto')
```

**Uso de internacionalización en vistas**

Para utilizar la internacionalización en vistas, puedes hacerlo mediante el uso del método `render` y el template tag `{% trans "mensaje" %}`. Por ejemplo:

```
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _

def my_view(request):
    return render(request, 'my_template.html', {'message': _('Hola, mundo!')})
```

**Uso de internacionalización en modelos**

Para utilizar la internacionalización en modelos, puedes hacerlo mediante el uso del método `__str__` o `__unicode__`. Por ejemplo:

```
from django.db import models
from django.utils.translation import gettext_lazy as _

class MyModel(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return _('Registro de {0} ({1})').format(self.name, self.email)
```

En este capítulo, hemos explorado cómo internacionalizar y localizar tu aplicación web en Django. Es importante recordar que la internacionalización y localización son fundamentales para cualquier proyecto que desee alcanzar un público amplio y diverso. Al seguir estos pasos, podrás ofrecer una experiencia más personalizada y atractiva para tus usuarios en diferentes partes del mundo.

**Ejercicio**

* Crea un nuevo proyecto Django y configura la internacionalización.
* Crea un paquete de traducción para español argentino (es_AR).
* Traduce los mensajes básicos del proyecto (como "Hello, world!" al español argentino).
* Compila los archivos de traducción.
* Utiliza la internacionalización en un template y un formulario.

**Conclusión**

En este capítulo, hemos explorado cómo internacionalizar y localizar tu aplicación web en Django. Al seguir estos pasos, podrás ofrecer una experiencia más personalizada y atractiva para tus usuarios en diferentes partes del mundo. Recuerda que la internacionalización y localización son fundamentales para cualquier proyecto que desee alcanzar un público amplio y diverso.

**Siguiente capítulo**

En el próximo capítulo, exploraremos cómo utilizar Celery para realizar tareas asíncronas en Django. ¡Estás listo para aprender más sobre esta tecnología emocionante!