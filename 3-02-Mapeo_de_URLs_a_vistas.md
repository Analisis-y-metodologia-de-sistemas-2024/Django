**Capítulo 4: Vistas y URLs**

**Sección 1: Mapeo de URLs a vistas**

En el capítulo anterior, aprendimos cómo crear funciones de vista en Django para manejar las solicitudes HTTP y renderizar plantillas HTML. Sin embargo, Django necesita saber qué función de vista debe ser llamada cuando se recibe una solicitud HTTP. Esto es donde entran en juego los mapeos de URLs a vistas.

**¿Qué son los mapeos de URLs a vistas?**

Los mapeos de URLs a vistas son un mecanismo para asociar patrones de URL con funciones de vista. Cuando Django recibe una solicitud HTTP, analiza el patrón de la URL y llama a la función de vista correspondiente. De esta manera, podemos definir qué acciones debe realizar nuestra aplicación cuando se reciba una solicitud HTTP.

**Creando un mapeo de URLs a vistas**

Para crear un mapeo de URLs a vistas, debemos configurar el archivo `urls.py` en nuestra aplicación. Este archivo contiene la lista de patrones de URL y las funciones de vista asociadas.

Por ejemplo, supongamos que queremos crear una vista que renderice una página de inicio cuando se acceda a la ruta `/hello`. Primero, creamos una función de vista:
```python
# views.py
from django.shortcuts import render

def hello_view(request):
    return render(request, 'hello.html')
```
Luego, en el archivo `urls.py`, definimos el mapeo de URL correspondiente:
```python
# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello_view, name='hello'),
]
```
En este ejemplo, estamos definiendo un patrón de URL que coincide con la ruta `/hello`. Cuando se reciba una solicitud HTTP para esta ruta, Django llamará a la función `hello_view` y renderizará la plantilla `hello.html`.

**Argumentos en los mapeos de URLs a vistas**

Los mapeos de URLs a vistas también pueden recibir argumentos. Por ejemplo, supongamos que queremos crear una vista que muestre un mensaje personalizado cuando se acceda a la ruta `/hello/<nombre>`. En este caso, podemos definir el patrón de URL con un parámetro:
```python
# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('hello/<str:name>/', views.hello_view, name='hello'),
]
```
La función `hello_view` recibirá un argumento `name`, que se utilizará para personalizar el mensaje:
```python
# views.py
from django.shortcuts import render

def hello_view(request, name):
    return render(request, 'hello.html', {'name': name})
```
De esta manera, cuando se acceda a la ruta `/hello/Juan`, la función `hello_view` recibiría el argumento `Juan` y renderizaría la plantilla `hello.html` con un mensaje personalizado.

**Herencia en los mapeos de URLs a vistas**

Django también permite heredar patrones de URL de otras aplicaciones o módulos. Por ejemplo, supongamos que tenemos una aplicación `core` que contiene una vista `index_view` y queremos crear una nueva aplicación `blog` que herede este patrón de URL:
```python
# core/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
]

# blog/urls.py
from django.urls import include
from . import views

urlpatterns = [
    path('', include('core.urls')),
]
```
En este ejemplo, la aplicación `blog` incluye los patrones de URL de la aplicación `core` y puede acceder a la vista `index_view`. De esta manera, podemos reutilizar patrones de URL existentes en nuestras aplicaciones.

**Utilizando expresiones regulares en los mapeos de URLs a vistas**

Django también permite utilizar expresiones regulares para definir patrones de URL más complejos. Por ejemplo, supongamos que queremos crear una vista que renderice una página de búsqueda cuando se acceda a la ruta `/search/<palabra_clave>`. En este caso, podemos definir el patrón de URL con una expresión regular:
```python
# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('search/(?P<word>[a-zA-Z0-9]+)', views.search_view, name='search'),
]
```
La función `search_view` recibiría un argumento `word`, que se utilizará para realizar la búsqueda:
```python
# views.py
from django.shortcuts import render

def search_view(request, word):
    return render(request, 'search.html', {'word': word})
```
De esta manera, cuando se acceda a la ruta `/search/Juan`, la función `search_view` recibiría el argumento `Juan` y renderizaría la plantilla `search.html` con el resultado de la búsqueda.

**Conclusiones**

En este capítulo, hemos aprendido cómo crear mapeos de URLs a vistas en Django. Vimos cómo definir patrones de URL para asociar funciones de vista con solicitudes HTTP, cómo utilizar argumentos y herencia en los mapeos de URLs, y cómo utilizar expresiones regulares para definir patrones de URL más complejos.

En el próximo capítulo, exploraremos cómo utilizar plantillas HTML para renderizar contenido dinámico y cómo interactuar con bases de datos utilizando ORM.