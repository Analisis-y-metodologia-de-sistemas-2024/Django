**Capítulo 2: Modelos y Base de Datos**

**Introducción a los modelos de Django**

En el capítulo anterior, hemos explorado los conceptos básicos del marco web framework Django y su estructura general. En este capítulo, nos enfocaremos en uno de los componentes más importantes de Django: los modelos.

Los modelos son la base de todos los datos que se almacenan en una aplicación Django. Permiten definir las estructuras de los datos, como tables o colecciones, y establecer relaciones entre ellas. En este capítulo, profundizaremos en los conceptos básicos de los modelos, cómo se definen y cómo interactúan con la base de datos.

**¿Qué son los modelos?**

En Django, un modelo es una representación abstracta de una tabla o colección de datos en la base de datos. Los modelos se utilizan para definir la estructura de los datos, incluyendo los campos que contienen y las relaciones entre ellos. Los modelos también proporcionan métodos para crear, leer, actualizar y eliminar (CRUD) registros en la base de datos.

**Definición de un modelo**

Para definir un modelo en Django, debemos crear una clase que herede de `models.Model`. Esta clase se llama "modelo" y debe ser ubicada en el directorio `app/models.py` de nuestra aplicación. Por ejemplo:
```python
from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
```
En este ejemplo, estamos definiendo un modelo llamado `Autor` con tres campos: `nombre`, `apellido` y `email`. El campo `nombre` es de tipo cadena y tiene una longitud máxima de 100 caracteres. El campo `apellido` también es de tipo cadena y tiene una longitud máxima de 100 caracteres. El campo `email` es de tipo dirección de correo electrónico y se establece como único.

**Campos en los modelos**

Los campos son los componentes básicos de un modelo. En Django, hay varios tipos de campos que podemos utilizar para definir la estructura de nuestros datos. Algunos ejemplos incluyen:

* `CharField`: Un campo de tipo cadena.
* `IntegerField`: Un campo de tipo entero.
* `DateTimeField`: Un campo de tipo fecha y hora.
* `TextField`: Un campo de tipo texto largo.

En el ejemplo anterior, estamos utilizando tres campos: `CharField` para los campos `nombre` y `apellido`, y `EmailField` para el campo `email`.

**Relaciones entre modelos**

Los modelos en Django también pueden establecer relaciones entre ellos. Hay dos tipos de relaciones:

* `OneToOneField`: Una relación uno-a-uno, donde un registro en un modelo está relacionado con exactamente uno registro en otro modelo.
* `ForeignKey`: Una relación uno-a-muchos, donde un registro en un modelo puede estar relacionado con varios registros en otro modelo.

Por ejemplo:
```python
from django.db import models

class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
```
En este ejemplo, estamos definiendo un modelo `Libro` con un campo `autor` que se establece como una relación uno-a-muchos con el modelo `Autor`. Esto significa que cada libro está relacionado con exactamente un autor.

**Creación de instancias de modelos**

Para crear una instancia de un modelo en Django, podemos utilizar la clase `Model` y llamamos al método `objects.create()` para crear un nuevo registro. Por ejemplo:
```python
from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

autor1 = Autor.objects.create(nombre='John', apellido='Doe', email='johndoe@example.com')
```
En este ejemplo, estamos creando una instancia de la clase `Autor` y llamamos al método `objects.create()` para crear un nuevo registro en la base de datos.

**Lectura de instancias de modelos**

Para leer una instancia de un modelo en Django, podemos utilizar la clase `Model` y llamamos al método `objects.get()` para obtener un registro específico. Por ejemplo:
```python
from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

autor1 = Autor.objects.get(nombre='John', apellido='Doe')
```
En este ejemplo, estamos leyendo una instancia de la clase `Autor` y llamamos al método `objects.get()` para obtener el registro que coincide con los valores `nombre` y `apellido`.

**Actualización de instancias de modelos**

Para actualizar una instancia de un modelo en Django, podemos utilizar la clase `Model` y llamamos al método `save()` para guardar los cambios. Por ejemplo:
```python
from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

autor1 = Autor.objects.get(nombre='John', apellido='Doe')
autor1.email = 'johndoe2@example.com'
autor1.save()
```
En este ejemplo, estamos actualizando la instancia de la clase `Autor` y llamamos al método `save()` para guardar los cambios en la base de datos.

**Eliminación de instancias de modelos**

Para eliminar una instancia de un modelo en Django, podemos utilizar la clase `Model` y llamamos al método `delete()` para eliminar el registro. Por ejemplo:
```python
from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

autor1 = Autor.objects.get(nombre='John', apellido='Doe')
autor1.delete()
```
En este ejemplo, estamos eliminando la instancia de la clase `Autor` y llamamos al método `delete()` para eliminar el registro en la base de datos.

En resumen, los modelos en Django son una forma de definir la estructura de los datos y establecer relaciones entre ellos. En este capítulo, hemos explorado cómo se definen los modelos, qué campos pueden utilizarse y cómo interactúan con la base de datos. En el próximo capítulo, profundizaremos en las operaciones CRUD (Create, Read, Update, Delete) y cómo utilizarlos para manejar nuestros datos.

**Conclusión**

En este capítulo, hemos aprendido sobre los modelos en Django y cómo se utilizan para definir la estructura de los datos. Los modelos permiten establecer relaciones entre ellos y interactuar con la base de datos. En el próximo capítulo, exploraremos las operaciones CRUD y cómo utilizarlos para manejar nuestros datos.

**Ejercicios**

1. Crea un modelo llamado `Persona` con campos `nombre`, `apellido` y `email`.
2. Crea un modelo llamado `Direccion` con campos `calle`, `numero` y `ciudad`.
3. Establece una relación uno-a-muchos entre los modelos `Persona` y `Direccion`.

**Solución**

1.
```python
from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
```
2.
```python
from django.db import models

class Direccion(models.Model):
    calle = models.CharField(max_length=100)
    numero = models.IntegerField()
    ciudad = models.CharField(max_length=100)
```
3.
```python
from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)

class Direccion(models.Model):
    calle = models.CharField(max_length=100)
    numero = models.IntegerField()
    ciudad = models.CharField(max_length=100)
```
Espero que este capítulo te haya ayudado a entender los conceptos básicos de los modelos en Django. En el próximo capítulo, exploraremos las operaciones CRUD y cómo utilizarlos para manejar nuestros datos. ¡Hasta luego!