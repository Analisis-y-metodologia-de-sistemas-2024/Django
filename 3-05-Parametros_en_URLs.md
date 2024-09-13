**Parámetros en URLs**

En el capítulo anterior, hemos aprendido sobre el mapeo de URLs a vistas y los patrones de URL y expresiones regulares. Ahora, vamos a profundizar en uno de los aspectos más importantes del mapeo de URLs: los parámetros.

Los parámetros en URLs son una forma de pasar información adicional desde la URL hasta nuestra vista. Esto se logra mediante el uso de palabras clave en la ruta de la URL que se corresponden con los nombres de parámetros definidos en la vista.

**Definir Parámetros en la Vista**

Para definir un parámetro en una vista, debemos especificar un nombre de parámetro seguido de una corchete `<>` y el tipo de parámetro. Por ejemplo:
```
from django.urls import path
from . import views

urlpatterns = [
    path('article/<int:year>/', views.article, name='article'),
]
```
En este ejemplo, estamos definiendo un parámetro `year` que debe ser un entero (`int`). Esto significa que cuando se acceda a la URL `/article/2022/`, el valor `2022` se pasará como parámetro a la vista `article`.

**Parámetros en la Ruta**

En la ruta de la URL, podemos pasar los parámetros utilizando el siguiente formato:
```
/article/<year>/
```
Donde `<year>` es el nombre del parámetro que estamos definiendo. Cuando se acceda a esta URL, Django pasará el valor del parámetro como un objeto `HttpRequest` en la vista.

**Acceder a los Parámetros**

Para acceder a los parámetros en la vista, podemos utilizar la variable `request` y acceder al parámetro mediante su nombre. Por ejemplo:
```
from django.http import HttpResponse

def article(request, year):
    return HttpResponse(f'Article from {year}')
```
En este ejemplo, estamos definiendo una vista que recibe dos argumentos: `request` y `year`. El método `HttpResponse` devuelve un mensaje que incluye el valor del parámetro `year`.

**Tipos de Parámetros**

Django admite varios tipos de parámetros, incluyendo:

* `str`: Un string (cadena de caracteres)
* `int`: Un entero
* `float`: Un número decimal
* `path`: Una ruta relativa o absoluta
* `uuid`: Un identificador único
* `slug`: Un slug (una cadena de caracteres que se utiliza para identificar un objeto)

**Ejemplo: Parámetros en URLs con Tipos**

Supongamos que queremos definir una URL que recibe dos parámetros: `category` y `id`. El tipo de `category` es `str` y el tipo de `id` es `int`.
```
from django.urls import path
from . import views

urlpatterns = [
    path('products/<str:category>/<int:id>/', views.product, name='product'),
]
```
En este ejemplo, estamos definiendo dos parámetros: `category` y `id`. El tipo de `category` es `str` y el tipo de `id` es `int`.

**Parámetros en la Vista**

Para acceder a los parámetros en la vista, podemos utilizar la variable `request` y acceder al parámetro mediante su nombre. Por ejemplo:
```
from django.http import HttpResponse

def product(request, category, id):
    return HttpResponse(f'Product {category} with ID {id}')
```
En este ejemplo, estamos definiendo una vista que recibe tres argumentos: `request`, `category` y `id`. El método `HttpResponse` devuelve un mensaje que incluye los valores de los parámetros.

**Resumen**

En este capítulo, hemos aprendido sobre los parámetros en URLs. Los parámetros son una forma de pasar información adicional desde la URL hasta nuestra vista. Para definir un parámetro, debemos especificar un nombre de parámetro seguido de una corchete `<>` y el tipo de parámetro. En la ruta de la URL, podemos pasar los parámetros utilizando el siguiente formato: `<nombre_del_parametro>`. En la vista, podemos acceder a los parámetros mediante la variable `request`.

**Ejercicios**

1. Defina una URL que recibe un parámetro `name` del tipo `str`.
2. Defina una vista que imprima el valor del parámetro `name` en la salida.
3. Crea una ruta que reciba dos parámetros: `category` y `id`. El tipo de `category` es `str` y el tipo de `id` es `int`.
4. Defina una vista que imprima los valores de los parámetros `category` y `id` en la salida.
5. Crea una ruta que reciba un parámetro `slug` del tipo `slug`. ¿Cómo se podría acceder a este parámetro en la vista?