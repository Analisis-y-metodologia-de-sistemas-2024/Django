**Capítulo 6: Admin de Django - Inlines y edición en línea**

En este capítulo, vamos a profundizar en los inlines y la edición en línea en el administrador de Django. Los inlines son una herramienta poderosa que nos permite agregar campos adicionales a nuestros modelos en la pantalla de detalles del objeto, lo que facilita la edición de datos complejos. Además, veremos cómo aprovechar la edición en línea para mejorar la experiencia del usuario al interactuar con el administrador.

**Inlines**

Los inlines son una forma de agregar campos adicionales a los modelos en la pantalla de detalles del objeto en el administrador. Esto se logra mediante la creación de un inline formset, que es un conjunto de formularios relacionados con el modelo principal.

Para crear un inline formset, necesitamos definir un tipo de formulario especial llamado InlineFormSetFactory. Esta clase se encarga de crear los formularios inlines y gestionar las operaciones de creación, edición y eliminación de los objetos relacionados.

Vamos a ver un ejemplo de cómo crear un inline formset para el modelo `Book` con un campo adicional llamado `Author`. Primero, debemos definir el modelo `Book` con un campo many-to-one que apunta al modelo `Author`.

```python
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
```

Luego, podemos crear un inline formset para el modelo `Book` con el campo `author`.

```python
from django.contrib import admin
from .models import Book

class BookInline(admin.StackedInline):
    model = Book
    extra = 1

class BookAdmin(admin.ModelAdmin):
    inlines = [BookInline]
```

En este ejemplo, estamos creando un inline formset llamado `BookInline` que se encarga de gestionar los campos del modelo `Book`. El parámetro `extra=1` indica que se deben mostrar inicialmente dos formularios inlines adicionales.

**Edición en línea**

La edición en línea es una forma de mejorar la experiencia del usuario al interactuar con el administrador. En lugar de tener que navegar a una página separada para editar un objeto, podemos permitir que los usuarios editen objetos directamente en la pantalla de detalles del objeto.

Para habilitar la edición en línea, necesitamos definir un tipo de vista especial llamado ModelFormsetsView. Esta clase se encarga de gestionar las operaciones de creación y edición de los formularios inlines.

Vamos a ver un ejemplo de cómo crear una vista de edición en línea para el modelo `Book`.

```python
from django.contrib import admin
from .models import Book

class BookInline(admin.StackedInline):
    model = Book
    extra = 1

class BookAdmin(admin.ModelAdmin):
    inlines = [BookInline]

class BookEditView(ModelFormsetsView):
    formset_model = Book
    formset_queryset = Book.objects.filter(id=1)
```

En este ejemplo, estamos creando una vista de edición en línea llamada `BookEditView` que se encarga de gestionar los formularios inlines para el modelo `Book`. El parámetro `formset_model` indica qué modelo se debe editar, y el parámetro `formset_queryset` especifica qué objetos se deben mostrar.

**Conclusión**

En este capítulo, hemos aprendido a crear inlines y edición en línea en el administrador de Django. Los inlines nos permiten agregar campos adicionales a nuestros modelos en la pantalla de detalles del objeto, lo que facilita la edición de datos complejos. La edición en línea es una forma de mejorar la experiencia del usuario al interactuar con el administrador, y podemos habilitarla mediante la definición de un tipo de vista especial.

**Próximo capítulo**

En el próximo capítulo, vamos a explorar las vistas de listado en Django, que nos permiten mostrar listados de objetos en el administrador. Veremos cómo crear vistas de listado personalizadas y cómo utilizar los parámetros de filtrado y ordenamiento para mejorar la experiencia del usuario.

**Referencias**

* Documentación oficial de Django: "Admin documentation"
* Documentación oficial de Django: "Formsets and inlines"

**Ejemplos de código**

* Ejemplo 1: Crear un inline formset
```python
from django.contrib import admin
from .models import Book

class BookInline(admin.StackedInline):
    model = Book
    extra = 1

class BookAdmin(admin.ModelAdmin):
    inlines = [BookInline]
```
* Ejemplo 2: Crear una vista de edición en línea
```python
from django.contrib import admin
from .models import Book

class BookInline(admin.StackedInline):
    model = Book
    extra = 1

class BookAdmin(admin.ModelAdmin):
    inlines = [BookInline]

class BookEditView(ModelFormsetsView):
    formset_model = Book
    formset_queryset = Book.objects.filter(id=1)
```