**Capítulo 5: Django ORM Avanzado**

En este capítulo, vamos a profundizar en los aspectos más avanzados del ORM (Object-Relational Mapping) de Django. Aprendimos sobre la creación de modelos y campos, relaciones entre modelos y migraciones en el capítulo anterior. En este capítulo, exploraremos cómo utilizar el ORM para realizar operaciones complejas y avanzadas con nuestra base de datos.

### 5.1. Agrupaciones y Consultas Avanzadas

Uno de los aspectos más poderosos del ORM es la capacidad de realizar consultas avanzadas utilizando métodos como `filter()`, `exclude()` y `annotate()`. Estos métodos permiten filtrar resultados, excluir filas que no cumplan con ciertas condiciones y agregar información adicional a las filas resultado.

Por ejemplo, supongamos que queremos obtener una lista de todos los usuarios que han comprado un producto en particular. Podríamos utilizar el método `filter()` para hacerlo:
```python
from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

class Compra(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_compra = models.DateTimeField(auto_now_add=True)

# Obtener la lista de usuarios que han comprado un producto
producto = Producto.objects.get(nombre='Producto X')
usuarios_que_han_comprado = Compra.objects.filter(producto=producto).values_list('usuario', flat=True).distinct()
```
En este ejemplo, estamos utilizando el método `filter()` para obtener una lista de filas en la tabla `Compra` que tienen un producto específico. Luego, estamos utilizando el método `values_list()` para obtener solo los valores de la columna `usuario`, y el parámetro `flat=True` para obtener una lista de valores en lugar de una lista de tuplas.

### 5.2. Agrupaciones y Consultas con Agregados

El ORM también permite realizar consultas que incluyen agregados, como suma o conteo de filas. Estos agregados se realizan utilizando el método `aggregate()`.

Por ejemplo, supongamos que queremos obtener la suma total del precio de todos los productos vendidos en un período determinado:
```python
from django.db.models import Sum

# Obtener la suma total del precio de todos los productos vendidos en un período determinado
fecha_inicio = datetime.date(2022, 1, 1)
fecha_fin = datetime.date(2022, 12, 31)

productos_vendidos = Compra.objects.filter(fecha_compra__range=(fecha_inicio, fecha_fin)).values('producto').annotate(total_precio=Sum('producto__precio'))
```
En este ejemplo, estamos utilizando el método `filter()` para obtener una lista de filas en la tabla `Compra` que tienen fechas de compra dentro del período determinado. Luego, estamos utilizando el método `values()` para obtener solo los valores de la columna `producto`, y el método `annotate()` para agregar un campo calculado llamado `total_precio`. El campo `total_precio` es calculado sumando el precio de cada producto.

### 5.3. Consultas con Subconsultas

El ORM también permite realizar consultas que incluyen subconsultas, como obtener la lista de productos vendidos por un usuario específico:
```python
# Obtener la lista de productos vendidos por un usuario específico
usuario = User.objects.get(id=1)
productos_vendidos = Compra.objects.filter(usuario=usuario).values('producto').distinct()
```
En este ejemplo, estamos utilizando el método `filter()` para obtener una lista de filas en la tabla `Compra` que tienen un usuario específico. Luego, estamos utilizando el método `values()` para obtener solo los valores de la columna `producto`, y el parámetro `distinct()` para eliminar duplicados.

### 5.4. Consultas con Join

El ORM también permite realizar consultas que incluyen join, como obtener la lista de productos vendidos por un usuario específico junto con su información:
```python
# Obtener la lista de productos vendidos por un usuario específico junto con su información
usuario = User.objects.get(id=1)
productos_vendidos = Compra.objects.select_related('producto').filter(usuario=usuario).values('producto__nombre', 'producto__precio', 'fecha_compra')
```
En este ejemplo, estamos utilizando el método `select_related()` para especificar que queremos obtener la información de la tabla `Producto` asociada a la tabla `Compra`. Luego, estamos utilizando el método `filter()` para obtener una lista de filas en la tabla `Compra` que tienen un usuario específico. Finalmente, estamos utilizando el método `values()` para obtener solo los valores de las columnas deseadas.

### 5.5. Consultas con EXISTS y NOT EXISTS

El ORM también permite realizar consultas que incluyen EXISTS y NOT EXISTS, como obtener la lista de usuarios que han comprado un producto:
```python
# Obtener la lista de usuarios que han comprado un producto
producto = Producto.objects.get(nombre='Producto X')
usuarios_que_han_comprado = User.objects.filter(exists=Compra.objects.filter(producto=producto)))
```
En este ejemplo, estamos utilizando el método `filter()` para obtener una lista de filas en la tabla `User` que tienen un registro en la tabla `Compra` que tiene el producto específico.

### 5.6. Consultas con IN y NOT IN

El ORM también permite realizar consultas que incluyen IN y NOT IN, como obtener la lista de usuarios que han comprado productos en una lista determinada:
```python
# Obtener la lista de usuarios que han comprado productos en una lista determinada
productos = [Producto.objects.get(nombre='Producto X'), Producto.objects.get(nombre='Producto Y')]
usuarios_que_han_comprado = User.objects.filter(Compra.objects.filter(producto__in=productos)))
```
En este ejemplo, estamos utilizando el método `filter()` para obtener una lista de filas en la tabla `User` que tienen registros en la tabla `Compra` que incluyen productos en la lista determinada.

### 5.7. Consultas con LIKE y NOT LIKE

El ORM también permite realizar consultas que incluyen LIKE y NOT LIKE, como obtener la lista de usuarios que han comprado productos con un nombre que contiene una cadena específica:
```python
# Obtener la lista de usuarios que han comprado productos con un nombre que contiene una cadena específica
cadena = 'Producto X'
usuarios_que_han_comprado = User.objects.filter(Compra.objects.filter(producto__nombre__icontains=cadena)))
```
En este ejemplo, estamos utilizando el método `filter()` para obtener una lista de filas en la tabla `User` que tienen registros en la tabla `Compra` que incluyen productos con nombres que contienen la cadena específica.

En este capítulo, hemos explorado los aspectos más avanzados del ORM de Django, incluyendo agrupaciones y consultas avanzadas, consultas con agregados, consultas con subconsultas, consultas con join, consultas con EXISTS y NOT EXISTS, consultas con IN y NOT IN, y consultas con LIKE y NOT LIKE. Estos métodos permiten realizar operaciones complejas y avanzadas con nuestra base de datos, lo que nos permite crear aplicaciones más poderosas y flexibles.