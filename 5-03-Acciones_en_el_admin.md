**Acciones en el Admin**

En el capítulo anterior, exploramos la personalización del admin y cómo podemos adaptar nuestro sitio de administración a nuestras necesidades específicas. Ahora, vamos a profundizar en las acciones que podemos realizar dentro del admin, como crear, leer, actualizar y eliminar objetos.

**Crear un nuevo objeto**

Una de las acciones más comunes en el admin es crear nuevos objetos. Django proporciona una forma fácil de hacer esto mediante la creación de formularios que permiten al administrador ingresar datos para crear un nuevo objeto.

Por ejemplo, supongamos que estamos creando una aplicación para gestionar libros y queremos agregar una nueva opción para agregar un libro a nuestra base de datos. Primero, debemos definir el modelo para nuestro libro en el archivo `models.py`:
```python
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_date = models.DateField()
```
Luego, debemos crear un administrador para nuestro modelo en el archivo `admin.py`:
```python
from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_date')
```
En este ejemplo, estamos registrando el modelo `Book` con el administrador y definimos qué campos mostrar en la lista de objetos.

Ahora, cuando nos dirigimos al admin, podemos ver un botón "Add book" (Agregar libro) en la parte superior derecha de la pantalla. Al hacer clic en ese botón, se abre un formulario para ingresar los datos del nuevo libro:
```html
<form method="post">
    <label for="id_title">Title:</label>
    <input type="text" name="title" required><br><br>
    <label for="id_author">Author:</label>
    <input type="text" name="author" required><br><br>
    <label for="id_publication_date">Publication Date:</label>
    <input type="date" name="publication_date" required><br><br>
    <input type="submit" value="Save">
</form>
```
Al enviar el formulario, Django crea un nuevo objeto `Book` en nuestra base de datos con los datos ingresados.

**Leer objetos**

Otra acción común es leer objetos existentes. En el admin, podemos ver una lista de todos los objetos que cumplen con ciertas condiciones y podemos filtrar la lista según diferentes criterios.

Por ejemplo, supongamos que queremos ver la lista de libros publicados en un año determinado. Podemos hacer esto agregando un campo `publication_date` a nuestra vista de lista:
```python
from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_date')
    date_hierarchy = 'publication_date'
```
En este ejemplo, estamos agregando un campo `date_hierarchy` que permite filtrar la lista de libros según el año y mes de publicación.

**Actualizar objetos**

Una acción importante es actualizar los objetos existentes. En el admin, podemos hacer esto mediante un formulario similar al que utilizamos para crear nuevos objetos.

Por ejemplo, supongamos que queremos actualizar el título de un libro existente. Podemos hacer esto navegando a la página del libro en cuestión y haciendo clic en el botón "Edit" (Editar):
```html
<form method="post">
    <label for="id_title">Title:</label>
    <input type="text" name="title" value="{{ book.title }}"><br><br>
    <label for="id_author">Author:</label>
    <input type="text" name="author" value="{{ book.author }}"><br><br>
    <label for="id_publication_date">Publication Date:</label>
    <input type="date" name="publication_date" value="{{ book.publication_date }}"><br><br>
    <input type="submit" value="Save Changes">
</form>
```
Al enviar el formulario, Django actualiza los datos del libro existente con los valores ingresados.

**Eliminar objetos**

La última acción importante es eliminar objetos existentes. En el admin, podemos hacer esto mediante un botón "Delete" (Borrar) que se encuentra en la página de detalles de cada objeto.

Por ejemplo, supongamos que queremos eliminar un libro existente. Podemos hacer esto navegando a la página del libro y haciendo clic en el botón "Delete":
```html
<form method="post">
    <input type="submit" value="Delete">
</form>
```
Al enviar el formulario, Django elimina el objeto `Book` de nuestra base de datos.

**Conclusión**

En este capítulo, hemos explorado las acciones que podemos realizar dentro del admin, como crear, leer, actualizar y eliminar objetos. También hemos visto cómo personalizar nuestro sitio de administración para adaptarlo a nuestras necesidades específicas.

Es importante destacar que el admin es una herramienta poderosa y flexible que nos permite gestionar nuestra aplicación con facilidad y eficiencia. Sin embargo, también es importante recordar que el admin no debe ser utilizado como una forma de acceso directo a la base de datos, sino más bien como una interfaz para realizar operaciones de alta nivel.

En el próximo capítulo, exploraremos cómo utilizar las APIs de Django para interactuar con nuestra aplicación y crear interfaces de usuario personalizadas.