**Introducción a las pruebas en Django**

En el desarrollo de aplicaciones web con Django, es fundamental la realización de pruebas para asegurarse de que el código funciona correctamente y se ajusta a los requisitos establecidos. En este capítulo, nos enfocaremos en la introducción a las pruebas en Django, explorando sus fundamentos y características clave.

**¿Por qué es importante probar nuestro código?**

Probar nuestro código es una parte fundamental del proceso de desarrollo de software. Algunas razones importantes para probar nuestro código incluyen:

* **Asegurar la calidad**: Las pruebas ayudan a detectar errores y bugs en el código, lo que garantiza que nuestra aplicación funcione correctamente.
* **Reducir el riesgo**: Al probar nuestro código, reducimos el riesgo de lanzar una aplicación defectuosa, lo que puede costar tiempo y dinero para arreglar.
* **Mejorar la confianza**: Las pruebas nos permiten verificar que nuestro código se ajusta a los requisitos establecidos, lo que mejora nuestra confianza en la aplicación.

**¿Qué tipo de pruebas existen?**

Existen varios tipos de pruebas que podemos realizar en Django:

* **Unittests**: Son pruebas unitarias que se enfocan en probar individualmente las funciones y métodos de nuestras aplicaciones.
* **Integración tests**: Son pruebas que se enfocan en verificar la integración entre diferentes partes de nuestra aplicación.
* **Functional tests**: Son pruebas que se enfocan en verificar el comportamiento funcional de nuestra aplicación, es decir, su capacidad para realizar una tarea específica.

**Configuración básica**

Para empezar a probar nuestro código con Django, debemos configurar nuestras pruebas. Primero, necesitamos crear un archivo `tests.py` en la raíz de nuestro proyecto:
```python
# tests.py
import unittest

from django.test import TestCase

class MyTestCase(TestCase):
    def test_my_function(self):
        # Aquí va el código para probar nuestra función
        pass
```
En este archivo, estamos creando una clase que hereda de `unittest.TestCase`. La clase contiene un método `test_my_function`, que es donde podemos escribir nuestro código de prueba.

**Estructura de una prueba**

Una estructura básica de una prueba en Django se compone de:

1. **Setup**: Se ejecuta antes de la prueba y se encarga de configurar el entorno.
2. **Test**: Es el cuerpo principal de la prueba, donde escribimos nuestro código para probar.
3. **Teardown**: Se ejecuta después de la prueba y se encarga de limpiar el entorno.

**Ejemplos de pruebas**

A continuación, te presento algunos ejemplos de pruebas en Django:

### Prueba de una función

Supongamos que tenemos una función llamada `add` que suma dos números:
```python
# models.py
from django.db import models

def add(x, y):
    return x + y
```
Podemos probar esta función con la siguiente prueba:
```python
# tests.py
import unittest

from django.test import TestCase
from .models import add

class TestAddFunction(TestCase):
    def test_add_function(self):
        result = add(2, 3)
        self.assertEqual(result, 5)
```
En este ejemplo, estamos creando una prueba que verifica que la función `add` devuelve el resultado correcto (en este caso, 5) cuando se le pasan los argumentos 2 y 3.

### Prueba de una vista

Supongamos que tenemos una vista llamada `my_view` que muestra un mensaje:
```python
# views.py
from django.shortcuts import render

def my_view(request):
    return render(request, 'my_template.html', {'message': 'Hello, world!'})
```
Podemos probar esta vista con la siguiente prueba:
```python
# tests.py
import unittest

from django.test import TestCase
from .views import my_view

class TestMyView(TestCase):
    def test_my_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Hello, world!')
```
En este ejemplo, estamos creando una prueba que verifica que la vista `my_view` devuelve un estado de respuesta HTTP 200 y que el contenido de la página contiene el mensaje "Hello, world!".

**Conclusión**

En este capítulo, hemos explorado los fundamentos de las pruebas en Django. Hemos visto cómo crear archivos de prueba, estructurar nuestras pruebas y escribir código para probar diferentes partes de nuestra aplicación. Es importante recordar que las pruebas son una parte fundamental del proceso de desarrollo de software y que nos ayudan a asegurarnos de que nuestro código funciona correctamente.

**Ejercicio**

* Crea un archivo `tests.py` en la raíz de tu proyecto y agrega una prueba para probar una función simple.
* Modifica la prueba para verificar que la función devuelve el resultado correcto.
* Agrega una prueba para probar una vista que muestra un mensaje.

**Siguiente capítulo**

En el próximo capítulo, exploraremos cómo escribir pruebas de integración y funcionalidad en Django. ¡Vamos a ver cómo podemos probar nuestra aplicación de manera más exhaustiva!