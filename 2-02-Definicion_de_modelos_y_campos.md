**Capítulo 5: Modelos y Base de Datos**

En el capítulo anterior, exploramos la introducción a los modelos de Django, donde vimos cómo crear objetos en Python que representan datos almacenados en una base de datos. En este capítulo, profundizaremos en la definición de modelos y campos, y cómo estos conceptos se relacionan entre sí para crear una estructura sólida para nuestras aplicaciones.

**Definición de modelos**

En Django, un modelo es una representación abstracta de una entidad en la base de datos. Estas entidades pueden ser personas, productos, eventos, o cualquier otra cosa que desee almacenar y manipular en su aplicación. Los modelos se definen utilizando clases en Python que heredan de `django.db.models.Model`.

Cada modelo representa una tabla en la base de datos, y cada instancia del modelo (o "objeto") es una fila en esa tabla. Los campos del modelo, que discutiremos a continuación, determinan las columnas en la tabla.

**Definición de campos**

Un campo es una característica o atributo de un modelo que almacena datos. En Django, los campos se definen utilizando la clase `django.db.models.Field` y sus hijos.

Hay varios tipos de campos disponibles en Django, cada uno con su propio uso y propósito:

* **CharField**: Almacena cadenas de texto.
* **IntegerField**: Almacena números enteros.
* **DateTimeField**: Almacena fechas y horas.
* **BooleanField**: Almacena valores booleanos (verdadero o falso).
* **ForeignKey**: Establece una relación entre dos modelos.

Cada campo en un modelo tiene varios atributos que podemos configurar:

* **name**: El nombre del campo, que se utiliza para acceder a sus valores.
* **verbose_name**: Un nombre más descriptivo del campo, que se muestra en las interfaces de usuario.
* **default**: Un valor predeterminado que se asigna al campo si no se proporciona un valor explícito.
* **blank**: Si es verdadero, el campo puede ser vacío. Si es falso, el campo debe tener un valor.

**Ejemplo: Definición de un modelo y campos**

Supongamos que estamos creando una aplicación para un blog. Queremos almacenar información sobre los autores de los artículos. Podríamos definir un modelo `Author` con los siguientes campos:
```python
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True)
```
En este ejemplo, estamos definiendo un modelo `Author` con tres campos:

* **name**: Un campo de cadena de texto que almacena el nombre del autor.
* **email**: Un campo de correo electrónico único que almacena la dirección de correo electrónico del autor.
* **bio**: Un campo de texto que almacena una breve biografía del autor. El campo `blank=True` indica que este campo puede ser vacío.

**Relaciones entre modelos**

Los modelos en Django pueden establecer relaciones con otros modelos mediante el uso de campos relacionados, como `ForeignKey`. Estas relaciones permiten a los modelos interactuar y acceder a datos de otros modelos.

Supongamos que queremos agregar una relación entre el modelo `Author` y un modelo `Article`. Podríamos definir un campo `author` en el modelo `Article` que hace referencia al modelo `Author`:
```python
from django.db import models

class Author(models.Model):
    # ...

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
```
En este ejemplo, estamos definiendo un campo `author` en el modelo `Article` que hace referencia al modelo `Author`. El parámetro `on_delete=models.CASCADE` indica qué hacer si se elimina un autor asociado: eliminar automáticamente los artículos relacionados con ese autor.

**Conclusión**

En este capítulo, hemos profundizado en la definición de modelos y campos en Django. Vimos cómo crear modelos que representan entidades en la base de datos y campos que almacenan datos. También exploramos las relaciones entre modelos y cómo establecer relaciones entre ellos mediante el uso de campos relacionados.

En el próximo capítulo, examinaremos cómo interactuar con la base de datos utilizando el ORM de Django y crear consultas para recuperar y manipular los datos almacenados en nuestra aplicación.