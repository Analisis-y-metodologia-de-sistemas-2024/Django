**Capítulo 9: Manejo de Archivos Estáticos y Media**

**Sección 1: Manejo de Archivos Subidos por Usuarios**

El manejo de archivos subidos por usuarios es un tema crucial en la creación de aplicaciones web que requieren la interacción con archivos. En Django, se pueden subir archivos a una aplicación mediante el uso del campo `FileField` o `ImageField` en los modelos.

Cuando se crea un modelo con un campo `FileField`, Django crea automáticamente una instancia de la clase `FileSystemStorage` para almacenar los archivos subidos. Esta instancia se encarga de guardar los archivos en el sistema de archivos local y proporciona métodos para leer y escribir archivos.

Para empezar, necesitamos crear un modelo que tenga un campo `FileField`. Vamos a crear un modelo llamado `Archivo` con un campo `file` de tipo `FileField`.
```python
from django.db import models

class Archivo(models.Model):
    file = models.FileField(upload_to='archivos/')
```
El parámetro `upload_to` especifica la ruta en donde se almacenarán los archivos subidos. En este caso, se almacenarán en una carpeta llamada `archivos`.

Ahora, necesitamos crear un formulario para subir archivos a nuestra aplicación. Vamos a crear un formulario llamado `ArchivoForm` que tenga un campo `file`.
```python
from django import forms
from .models import Archivo

class ArchivoForm(forms.ModelForm):
    class Meta:
        model = Archivo
        fields = ('file',)
```
El formulario `ArchivoForm` utiliza la clase `ModelForm` de Django para crear un formulario basado en el modelo `Archivo`. El campo `fields` especifica que solo se va a mostrar el campo `file`.

Para subir archivos, necesitamos crear una vista que maneje la solicitud y guarde el archivo en el sistema de archivos local. Vamos a crear una vista llamada `subir_archivo` que utilice el formulario `ArchivoForm`.
```python
from django.shortcuts import render, redirect
from .forms import ArchivoForm

def subir_archivo(request):
    if request.method == 'POST':
        form = ArchivoForm(request.POST, request.FILES)
        if form.is_valid():
            archivo = form.save()
            return redirect('archivo_detalle', pk=archivo.pk)
    else:
        form = ArchivoForm()
    return render(request, 'subir_archivo.html', {'form': form})
```
La vista `subir_archivo` utiliza el formulario `ArchivoForm` para validar la solicitud. Si la solicitud es válida, se guarda el archivo en el sistema de archivos local y se redirige a una página de detalles del archivo.

Para mostrar los archivos subidos, necesitamos crear una plantilla que muestre la lista de archivos y permita al usuario descargarlos o eliminarlos. Vamos a crear un template llamado `archivo_detalle.html` que muestre la información del archivo.
```html
{% extends 'base.html' %}

{% block content %}
  <h1>Detalle del Archivo</h1>
  <p>Nombre: {{ objeto.file.name }}</p>
  <p>Tamaño: {{ objeto.file.size }} bytes</p>
  <form method="post">
    {% csrf_token %}
    <input type="submit" value="Descargar">
  </form>
{% endblock %}
```
La plantilla `archivo_detalle.html` utiliza el template inheritance para heredar la plantilla base y mostrar la información del archivo. El campo `file.name` muestra el nombre del archivo, y el campo `file.size` muestra el tamaño del archivo.

Para eliminar archivos, necesitamos crear un view que elimine el archivo del sistema de archivos local. Vamos a crear una vista llamada `eliminar_archivo` que elimine el archivo.
```python
from django.shortcuts import render, redirect
from .models import Archivo

def eliminar_archivo(request, pk):
    archivo = Archivo.objects.get(pk=pk)
    archivo.file.delete()
    return redirect('subir_archivo')
```
La vista `eliminar_archivo` utiliza el método `delete` de la instancia `Archivo` para eliminar el archivo del sistema de archivos local. Luego, se redirige a la página de subida de archivos.

En resumen, en esta sección hemos visto cómo manejar archivos subidos por usuarios en Django utilizando el campo `FileField` y el formulario `ModelForm`. También hemos creado una vista para subir archivos y plantillas para mostrar la información del archivo y eliminarlo.

**Sección 2: Manejo de Archivos Subidos por Usuarios con Django Forms**

En esta sección, vamos a ver cómo manejar archivos subidos por usuarios utilizando Django forms. Django forms son un tipo de formulario que se pueden utilizar para validar y procesar datos de una forma más segura y eficiente.

Para empezar, necesitamos crear un formulario que permita al usuario subir un archivo. Vamos a crear un formulario llamado `ArchivoForm` que tenga un campo `file`.
```python
from django import forms
from .models import Archivo

class ArchivoForm(forms.Form):
    file = forms.FileField()
```
El formulario `ArchivoForm` utiliza el campo `FileField` de Django para crear un campo `file`.

Para validar la solicitud, necesitamos utilizar el método `is_valid()` del formulario. Si la solicitud es válida, se procesa el archivo y se guarda en el sistema de archivos local.
```python
from django.shortcuts import render, redirect
from .forms import ArchivoForm

def subir_archivo(request):
    if request.method == 'POST':
        form = ArchivoForm(request.POST, request.FILES)
        if form.is_valid():
            archivo = form.cleaned_data['file']
            # Procesar el archivo
            return redirect('archivo_detalle', pk=archivo.pk)
    else:
        form = ArchivoForm()
    return render(request, 'subir_archivo.html', {'form': form})
```
La vista `subir_archivo` utiliza el formulario `ArchivoForm` para validar la solicitud. Si la solicitud es válida, se procesa el archivo y se redirige a una página de detalles del archivo.

Para mostrar los archivos subidos, necesitamos crear una plantilla que muestre la lista de archivos y permita al usuario descargarlos o eliminarlos. Vamos a crear un template llamado `archivo_detalle.html` que muestre la información del archivo.
```html
{% extends 'base.html' %}

{% block content %}
  <h1>Detalle del Archivo</h1>
  <p>Nombre: {{ objeto.file.name }}</p>
  <p>Tamaño: {{ objeto.file.size }} bytes</p>
  <form method="post">
    {% csrf_token %}
    <input type="submit" value="Descargar">
  </form>
{% endblock %}
```
La plantilla `archivo_detalle.html` utiliza el template inheritance para heredar la plantilla base y mostrar la información del archivo. El campo `file.name` muestra el nombre del archivo, y el campo `file.size` muestra el tamaño del archivo.

Para eliminar archivos, necesitamos crear un view que elimine el archivo del sistema de archivos local. Vamos a crear una vista llamada `eliminar_archivo` que elimine el archivo.
```python
from django.shortcuts import render, redirect
from .models import Archivo

def eliminar_archivo(request, pk):
    archivo = Archivo.objects.get(pk=pk)
    archivo.file.delete()
    return redirect('subir_archivo')
```
La vista `eliminar_archivo` utiliza el método `delete` de la instancia `Archivo` para eliminar el archivo del sistema de archivos local. Luego, se redirige a la página de subida de archivos.

En resumen, en esta sección hemos visto cómo manejar archivos subidos por usuarios utilizando Django forms y validación de formularios. También hemos creado una vista para subir archivos y plantillas para mostrar la información del archivo y eliminarlo.

**Sección 3: Manejo de Archivos Subidos por Usuarios con Celery**

En esta sección, vamos a ver cómo manejar archivos subidos por usuarios utilizando Celery, un framework de tareas asincrónicas. Celery permite ejecutar tareas en segundo plano, lo que puede ser útil cuando se necesitan procesar archivos grandes o realizar operaciones lentas.

Para empezar, necesitamos instalar y configurar Celery en nuestro proyecto.
```python
from celery import Celery

celery = Celery('tasks')
celery.conf.update({
    'CELERY_RESULT_BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
})
```
Luego, podemos crear una tarea que se encargue de procesar el archivo subido. Vamos a crear una tarea llamada `process_file` que tome un archivo como parámetro.
```python
from celery import shared_task

@shared_task
def process_file(file):
    # Procesar el archivo
    return {'status': 'ok'}
```
La tarea `process_file` utiliza el decorador `@shared_task` para marcarla como una tarea compartida. Luego, podemos invocar la tarea desde nuestro view y pasarle el archivo subido como parámetro.
```python
from django.shortcuts import render, redirect
from .tasks import process_file

def subir_archivo(request):
    if request.method == 'POST':
        file = request.FILES['file']
        # Invocar la tarea para procesar el archivo
        process_file.delay(file)
        return redirect('archivo_detalle', pk=file.pk)
    else:
        form = ArchivoForm()
    return render(request, 'subir_archivo.html', {'form': form})
```
La vista `subir_archivo` utiliza el método `delay` de la tarea `process_file` para invocarla en segundo plano y pasarle el archivo subido como parámetro. Luego, se redirige a la página de detalles del archivo.

Para mostrar los archivos subidos, necesitamos crear una plantilla que muestre la lista de archivos y permita al usuario descargarlos o eliminarlos. Vamos a crear un template llamado `archivo_detalle.html` que muestre la información del archivo.
```html
{% extends 'base.html' %}

{% block content %}
  <h1>Detalle del Archivo</h1>
  <p>Nombre: {{ objeto.file.name }}</p>
  <p>Tamaño: {{ objeto.file.size }} bytes</p>
  <form method="post">
    {% csrf_token %}
    <input type="submit" value="Descargar">
  </form>
{% endblock %}
```
La plantilla `archivo_detalle.html` utiliza el template inheritance para heredar la plantilla base y mostrar la información del archivo. El campo `file.name` muestra el nombre del archivo, y el campo `file.size` muestra el tamaño del archivo.

Para eliminar archivos, necesitamos crear un view que elimine el archivo del sistema de archivos local. Vamos a crear una vista llamada `eliminar_archivo` que elimine el archivo.
```python
from django.shortcuts import render, redirect
from .models import Archivo

def eliminar_archivo(request, pk):
    archivo = Archivo.objects.get(pk=pk)
    archivo.file.delete()
    return redirect('subir_archivo')
```
La vista `eliminar_archivo` utiliza el método `delete` de la instancia `Archivo` para eliminar el archivo del sistema de archivos local. Luego, se redirige a la página de subida de archivos.

En resumen, en esta sección hemos visto cómo manejar archivos subidos por usuarios utilizando Celery y tareas asincrónicas. También hemos creado una vista para subir archivos y plantillas para mostrar la información del archivo y eliminarlo.