**Capítulo 7: Templates y Formularios - Sistema de Templates de Django**

En el capítulo anterior, vimos cómo utilizar los templates para separar la lógica de negocio del diseño visual de nuestra aplicación web. En este capítulo, profundizaremos en el sistema de templates de Django, que nos brinda una forma poderosa y flexible de gestionar nuestros templates.

**¿Qué son los templates?**

Un template es un archivo HTML que contiene lugares vacíos para datos dinámicos. Cuando se renderiza un template, Django reemplaza estos lugares vacíos con los datos proporcionados por el desarrollador. Los templates permiten separar la lógica de negocio del diseño visual de nuestra aplicación web, lo que facilita su mantenimiento y actualización.

**¿Qué es el sistema de templates de Django?**

El sistema de templates de Django es un conjunto de herramientas que nos permiten crear, editar y renderizar nuestros templates. Está basado en el lenguaje de plantillas templating, que nos permite definir lugares vacíos para datos dinámicos utilizando sintaxis especial.

**Elementos básicos del sistema de templates**

Para trabajar con los templates en Django, debemos entender algunos conceptos básicos:

* **Templates**: Los templates son archivos HTML que contienen lugares vacíos para datos dinámicos.
* **Variables**: Las variables son valores que se pueden asignar a los lugares vacíos en un template. Pueden ser strings, números, booleanos, listas o objetos complejos.
* **Tags**: Los tags (también conocidos como "directivas") son instrucciones que se pueden utilizar dentro de un template para realizar acciones específicas, como iterar sobre una lista de datos o mostrar mensajes de error.
* **Filters**: Los filters (también conocidos como "filtros") son funciones que se pueden aplicar a variables para transformarlas en formato deseado. Por ejemplo, podemos utilizar un filter para convertir un valor numérico a una cadena.

**Creación y edición de templates**

Para crear un nuevo template en Django, debemos crear un archivo HTML en la carpeta `templates` del proyecto. El nombre del archivo debe seguir el siguiente patrón: `{aplicación}_/{plantilla}.html`, donde `{aplicación}` es el nombre de nuestra aplicación y `{plantilla}` es el nombre de nuestro template.

Por ejemplo, si queremos crear un template para una aplicación llamada `blog` que se llama `index.html`, debemos crear un archivo llamado `blog/index.html` en la carpeta `templates`.

Para editar un template, podemos utilizar cualquier editor de texto o un IDE como PyCharm. Es importante recordar que los templates deben ser estáticos y no contener código Python.

**Renderización de templates**

Para renderizar un template, debemos utilizar el objeto `RequestContext` que nos proporciona Django. El objeto `RequestContext` nos permite acceder a variables y objetos del contexto actual, como la solicitud HTTP y los datos de la base de datos.

Por ejemplo, si queremos renderizar un template llamado `index.html` con una variable llamada `titulo`, podemos utilizar el siguiente código:
```python
from django.shortcuts import render

def index(request):
    titulo = "Bienvenido a mi blog"
    return render(request, 'blog/index.html', {'titulo': titulo})
```
En este ejemplo, estamos creando una vista (`index`) que se encarga de renderizar un template llamado `index.html` con la variable `titulo`. El objeto `RequestContext` nos permite acceder a la solicitud HTTP y los datos de la base de datos.

**Tags y filters**

Los tags y filters son elementos básicos del sistema de templates de Django. Los tags permiten realizar acciones específicas dentro de un template, mientras que los filters permiten transformar variables en formato deseado.

Aquí hay algunos ejemplos de tags y filters:

* **Tag `for`:** Permite iterar sobre una lista de datos.
```html
{% for post in posts %}
    <h2>{{ post.titulo }}</h2>
    <p>{{ post.descripcion }}</p>
{% endfor %}
```
* **Filter `date`:** Permite mostrar la fecha en formato deseado.
```html
{{ fecha | date:"d/m/Y" }}
```
* **Tag `if`:** Permite realizar una condición booleana dentro de un template.
```html
{% if user.is_authenticated %}
    <p>Estás logueado</p>
{% else %}
    <p>No estás logueado</p>
{% endif %}
```
**Ventajas y desventajas**

El sistema de templates de Django tiene varias ventajas, como:

* Permite separar la lógica de negocio del diseño visual de nuestra aplicación web.
* Facilita el mantenimiento y actualización de nuestros templates.
* Permite utilizar variables y objetos complejos dentro de los templates.

También hay algunas desventajas, como:

* Requiere una buena comprensión de la sintaxis de plantillas templating.
* Puede ser complejo utilizar los tags y filters correctamente.
* No es adecuado para aplicaciones que requieren un alto nivel de personalización o flexibilidad.

**Conclusión**

En este capítulo, hemos profundizado en el sistema de templates de Django, que nos brinda una forma poderosa y flexible de gestionar nuestros templates. Hemos visto cómo crear y editar templates, renderizarlos con datos dinámicos y utilizar tags y filters para realizar acciones específicas.

Esperamos que esta información te haya sido útil. En el próximo capítulo, vamos a explorar los formularios en Django y ver cómo podemos utilizarlos para recopilar datos de nuestros usuarios.