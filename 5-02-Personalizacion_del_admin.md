**Capítulo 6: Admin de Django - Personalización**

En el capítulo anterior, exploramos la configuración del sitio de administración en Django y cómo personalizar el aspecto general de nuestra aplicación. En este capítulo, profundizaremos en las opciones de personalización más avanzadas que nos permiten adaptar el administrador a nuestras necesidades específicas.

**Configuración de la apariencia**

La primera forma de personalizar el admin es cambiando su apariencia. Esto se logra mediante la modificación de los estilos CSS y HTML utilizados en la aplicación. Para hacer esto, podemos utilizar el template `base.html` que se encuentra en la carpeta `templates/admin/` de nuestra aplicación.

En este archivo, encontramos los elementos básicos del admin, como el header, el footer y el contenido principal. Podemos personalizar estos elementos agregando nuestros propios estilos CSS o HTML. Por ejemplo, podemos cambiar el color de fondo o agregar un logo personalizado.

```python
<!-- templates/admin/base.html -->
<!DOCTYPE html>
<html>
<head>
    <title>My Admin</title>
    <style>
        body {
            background-color: #f2f2f2;
        }
    </style>
</head>
<body>
    <!-- Header -->
    <div class="header">
        <h1>My Admin</h1>
    </div>

    <!-- Contenido principal -->
    <div id="content">
        {% block content %}{% endblock %}
    </div>

    <!-- Footer -->
    <div class="footer">
        <p>&copy; 2023 My Company</p>
    </div>
</body>
</html>
```

En este ejemplo, estamos cambiando el color de fondo del body y agregando un header y footer personalizados.

**Personalización de los modelos**

La siguiente forma de personalizar el admin es cambiando la forma en que se muestran nuestros modelos. Esto se logra mediante la creación de formularios y vistas personalizados para cada modelo.

Por ejemplo, supongamos que tenemos un modelo `Book` con campos como `title`, `author` y `published_date`. Podemos crear un formulario personalizado para este modelo agregando campos adicionales o cambiando el orden en que se muestran los campos.

Para hacer esto, debemos crear una clase `ModelForm` que herede de la clase base `django.forms.ModelForm`. En esta clase, podemos definir nuestros campos y metodos personalizados.

```python
# models.py
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()

# forms.py
from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author', 'published_date')
        widgets = {
            'published_date': forms.DateInput(format=('%Y-%m-%d'), attrs={'type': 'date'}),
        }
```

En este ejemplo, estamos agregando un campo `published_date` y cambiando el tipo de input para que sea un campo de fecha.

**Personalización de las vistas**

La siguiente forma de personalizar el admin es cambiando la forma en que se muestran nuestros modelos. Esto se logra mediante la creación de vistas personalizadas para cada modelo.

Por ejemplo, supongamos que queremos mostrar los libros ordenados por título en lugar de fecha de publicación. Podemos crear una vista personalizada que ordene los libros según nuestro criterio.

```python
# views.py
from django.shortcuts import render
from .models import Book

def book_list(request):
    books = Book.objects.all().order_by('title')
    return render(request, 'books.html', {'books': books})
```

En este ejemplo, estamos creando una vista que muestra los libros ordenados por título. Podemos luego agregar esta vista a nuestro archivo `urls.py` para que sea accesible desde el admin.

```python
# urls.py
from django.urls import path
from .views import book_list

urlpatterns = [
    path('books/', book_list, name='book_list'),
]
```

**Personalización de los templates**

La última forma de personalizar el admin es cambiando la forma en que se muestran nuestros modelos. Esto se logra mediante la creación de templates personalizados para cada modelo.

Por ejemplo, supongamos que queremos mostrar los libros en una lista con un diseño personalizado. Podemos crear un template personalizado que muestre los libros según nuestro criterio.

```python
<!-- templates/books.html -->
{% extends 'admin/base.html' %}

{% block content %}
    <h1>Lista de Libros</h1>
    <ul>
        {% for book in books %}
            <li>{{ book.title }} ({{ book.author }})</li>
        {% endfor %}
    </ul>
{% endblock %}
```

En este ejemplo, estamos creando un template que muestre los libros en una lista con título y autor. Podemos luego agregar este template a nuestro archivo `views.py` para que sea accesible desde el admin.

En resumen, la personalización del admin es un proceso importante para adaptar nuestra aplicación a nuestras necesidades específicas. Podemos cambiar la apariencia del admin mediante la modificación de los estilos CSS y HTML, personalizar los modelos agregando campos adicionales o cambiando el orden en que se muestran los campos, crear vistas personalizadas para cada modelo y cambiar la forma en que se muestran nuestros modelos mediante la creación de templates personalizados.

**Ejercicio**

En este ejercicio, te pedimos que personalices el admin de tu aplicación agregando estilos CSS y HTML personalizados. Agrega un logo personalizado al header del admin y cambia el color de fondo del body a un color de tu elección.

Además, crea un formulario personalizado para el modelo `Book` y agrega campos adicionales como `description` y `price`. Cambia el orden en que se muestran los campos y agrega un campo de búsqueda.

Finalmente, crea una vista personalizada para mostrar los libros ordenados por título y agrega esta vista a tu archivo `urls.py`.

**Solución**

Para resolver este ejercicio, debemos seguir los siguientes pasos:

1. Agregamos estilos CSS y HTML personalizados al template `base.html` del admin.
2. Creamos un formulario personalizado para el modelo `Book`.
3. Cambiamos el orden en que se muestran los campos y agregamos un campo de búsqueda.
4. Creamos una vista personalizada para mostrar los libros ordenados por título.
5. Agregamos esta vista a nuestro archivo `urls.py`.

La solución completa se puede ver a continuación:
```python
<!-- templates/admin/base.html -->
<!DOCTYPE html>
<html>
<head>
    <title>My Admin</title>
    <style>
        body {
            background-color: #f2f2f2;
        }
        .logo {
            float: left;
            margin: 10px;
        }
    </style>
</head>
<body>
    <!-- Header -->
    <div class="header">
        <h1><img src="/static/logo.png" class="logo"> My Admin</h1>
    </div>

    <!-- Contenido principal -->
    <div id="content">
        {% block content %}{% endblock %}
    </div>

    <!-- Footer -->
    <div class="footer">
        <p>&copy; 2023 My Company</p>
    </div>
</body>
</html>
```

```python
# forms.py
from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author', 'published_date', 'description', 'price')
        widgets = {
            'published_date': forms.DateInput(format=('%Y-%m-%d'), attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 5}),
            'price': forms.NumberInput(),
        }
```

```python
# views.py
from django.shortcuts import render
from .models import Book

def book_list(request):
    books = Book.objects.all().order_by('title')
    return render(request, 'books.html', {'books': books})

def book_search(request):
    q = request.GET.get('q')
    if q:
        books = Book.objects.filter(title__icontains=q)
    else:
        books = Book.objects.all()
    return render(request, 'books.html', {'books': books})
```

```python
# urls.py
from django.urls import path
from .views import book_list, book_search

urlpatterns = [
    path('books/', book_list, name='book_list'),
    path('books/search/', book_search, name='book_search'),
]
```

```python
<!-- templates/books.html -->
{% extends 'admin/base.html' %}

{% block content %}
    <h1>Lista de Libros</h1>
    <ul>
        {% for book in books %}
            <li>{{ book.title }} ({{ book.author }})</li>
        {% endfor %}
    </ul>

    <form method="get">
        <input type="text" name="q" placeholder="Buscar libros...">
        <button type="submit">Buscar</button>
    </form>
{% endblock %}
```

Esperamos que esta solución te ayude a personalizar el admin de tu aplicación. Recuerda que la personalización del admin es un proceso importante para adaptar tu aplicación a tus necesidades específicas. ¡Buena suerte!