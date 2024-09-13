**Capítulo 5: Templates y Formularios**

**Sección 2: Filtros y Tags de Template**

En el capítulo anterior, abordamos la creación y personalización de templates en Django. Ahora, vamos a profundizar en los filtros y tags que se pueden utilizar para darle más vida y funcionalidad a nuestros templates.

**1. Introducción**

Los filtros y tags son una forma de agregar lógica y funcionalidad a nuestros templates, sin tener que escribir código Python explícito. Los filtros se utilizan para transformar o procesar valores, mientras que los tags se utilizan para incluir contenido dinámico en nuestro template.

**2. Filtros**

Los filtros son una forma de aplicar lógica y operaciones a nuestros datos antes de mostrarlos en el template. Los filtros se definen utilizando la función `register_filter` de Django, y se pueden utilizar en los templates con la sintaxis `{{ valor|filtro }}`.

**Ejemplo: Filtro para formatear fechas**

Supongamos que queremos mostrar una fecha en formato humano (mes/día/año) en lugar del formato estándar (año-mes-día). Podríamos crear un filtro llamado `date_format` que tome la fecha como entrada y devuelva el valor formateado:
```python
from django import template

register = template.Library()

@register.filter
def date_format(date):
    return f"{date.month}/{date.day}/{date.year}"
```
En nuestro template, podríamos utilizar este filtro de la siguiente manera:
```html
<p>La fecha es: {{ fecha|date_format }}</p>
```
**Ejemplo: Filtro para capitalizar texto**

Supongamos que queremos capitalizar el primer caracter de un texto. Podríamos crear un filtro llamado `capitalize` que tome el texto como entrada y devuelva el valor capitalizado:
```python
from django import template

register = template.Library()

@register.filter
def capitalize(text):
    return text.capitalize()
```
En nuestro template, podríamos utilizar este filtro de la siguiente manera:
```html
<p>El texto es: {{ texto|capitalize }}</p>
```
**3. Tags**

Los tags son una forma de incluir contenido dinámico en nuestros templates. Los tags se definen utilizando la función `register_tag` de Django, y se pueden utilizar en los templates con la sintaxis `{% tag %}`.

**Ejemplo: Tag para mostrar un mensaje de bienvenida**

Supongamos que queremos mostrar un mensaje de bienvenida personalizado en nuestra página principal. Podríamos crear un tag llamado `welcome_message` que tome el nombre del usuario como entrada y devuelva el valor:
```python
from django import template

register = template.Library()

@register.tag(name='welcome_message')
def welcome_message(parser, token):
    return WelcomeMessageNode(token)
```
La clase `WelcomeMessageNode` se encargaría de obtener el nombre del usuario desde la solicitud actual y mostrar el mensaje de bienvenida:
```python
class WelcomeMessageNode(template.Node):
    def __init__(self, token):
        self.token = token

    def render(self, context):
        username = context['request'].user.username
        return f"¡Bienvenido(a) {username}!"
```
En nuestro template, podríamos utilizar este tag de la siguiente manera:
```html
<p>{% welcome_message %}</p>
```
**4. Conclusiones**

En este capítulo, hemos abordado los filtros y tags que se pueden utilizar para darle más vida y funcionalidad a nuestros templates en Django. Los filtros se utilizan para transformar o procesar valores, mientras que los tags se utilizan para incluir contenido dinámico en nuestro template.

**5. Ejercicios**

1. Crea un filtro llamado `length` que tome un texto como entrada y devuelva la cantidad de caracteres.
2. Crea un tag llamado `show_image` que tome el nombre de una imagen como entrada y muestre la imagen en el template.
3. Modifica el tag `welcome_message` para que también incluya el nombre del usuario en mayúsculas.

**6. Bibliografía**

* Documentación oficial de Django: <https://docs.djangoproject.com/en/3.2/>
* Tutorial de Django: <https://docs.djangoproject.com/en/3.2/intro/tutorial01/>

En el próximo capítulo, abordaremos la creación de formularios en Django y cómo utilizarlos para recopilar datos del usuario.