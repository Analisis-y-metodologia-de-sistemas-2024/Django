**Capítulo 5: Templates y Formularios**

**Herencia de Templates**

La herencia de templates es una característica fundamental en el sistema de templates de Django que permite crear plantillas más complejas a partir de otras plantillas existentes. Esto se logra mediante la utilización del atributo `extends` en el tag `<template>`. En este capítulo, profundizaremos en los conceptos y ejemplos prácticos de herencia de templates.

**Ventajas de la Herencia de Templates**

La herencia de templates ofrece varias ventajas:

* **Reutilización de Código**: Al crear una plantilla que hereda de otra, se puede reutilizar el código ya existente en lugar de tener que reimplementarlo.
* **Estructura Organizada**: La herencia de templates permite organizar el código de manera jerárquica, lo que facilita la lectura y mantenimiento del mismo.
* **Flexibilidad**: La herencia de templates permite crear plantillas más complejas que pueden ser utilizadas en diferentes contextos.

**Ejemplos de Herencia de Templates**

Supongamos que queremos crear una plantilla `base.html` que contenga el encabezado y el pie de página de nuestra aplicación web. Luego, creamos una plantilla `index.html` que hereda de `base.html` y agrega contenido específico para la página de inicio.

**base.html**
```html
<!DOCTYPE html>
<html>
<head>
    <title>My Web App</title>
</head>
<body>
    <header>
        <!-- Encabezado -->
    </header>
    <main>
        {% block content %}{% endblock %}
    </main>
    <footer>
        <!-- Pie de página -->
    </footer>
</body>
</html>
```
**index.html**
```html
{% extends "base.html" %}

{% block content %}
    <h1>Bienvenido a mi aplicación web!</h1>
    <p>Este es el contenido de la página de inicio.</p>
{% endblock %}
```
En este ejemplo, `index.html` hereda la estructura básica de `base.html`, pero sobreescribe el bloque `content` con su propio contenido. De esta manera, podemos reutilizar la plantilla `base.html` en diferentes páginas y solo necesitar modificaciones específicas para cada una.

**Herencia de Templates Anidados**

La herencia de templates no se limita a una sola nivel de profundidad. Puedes crear plantillas que heredan de otras plantillas que a su vez heredan de otras, creando una estructura jerárquica compleja.

Por ejemplo:
```html
# base.html
{% block content %}
    {% include "header.html" %}
    <main>
        {% block main_content %}{% endblock %}
    </main>
    {% include "footer.html" %}
{% endblock %}

# header.html
<h1>Bienvenido!</h1>

# footer.html
<p>Copyright 2023</p>

# index.html
{% extends "base.html" %}

{% block main_content %}
    <h2>Página de inicio</h2>
    <p>Este es el contenido de la página de inicio.</p>
{% endblock %}
```
En este ejemplo, `index.html` hereda la plantilla `base.html`, que a su vez incluye las plantillas `header.html` y `footer.html`. De esta manera, podemos crear una estructura jerárquica compleja que nos permite reutilizar el código en diferentes niveles.

**Tipos de Herencia de Templates**

Existen dos tipos de herencia de templates:

* **Herencia Anidada**: La plantilla hija hereda la estructura y los bloques de la plantilla padre.
* **Herencia Paralela**: La plantilla hija puede incluir contenido paralelo a la plantilla padre, sin necesidad de heredar su estructura.

**Conclusiones**

La herencia de templates es una característica fundamental en el sistema de templates de Django que permite crear plantillas más complejas y reutilizar código. Al entender cómo funciona la herencia de templates, podemos crear aplicaciones web más organizadas y flexibles. En el próximo capítulo, exploraremos cómo utilizar formularios en Django para recopilar datos de nuestros usuarios.

**Ejercicios**

1. Crea una plantilla `base.html` que contenga un encabezado y un pie de página.
2. Crea una plantilla `index.html` que herede la estructura básica de `base.html` y agrega contenido específico para la página de inicio.
3. Crea una plantilla `header.html` que contenga el título de la aplicación web.
4. Crea una plantilla `footer.html` que contenga la información de copyright.

**Resolución de Ejercicios**

Los ejercicios se resuelven en el código Python y HTML que se muestra a continuación:

**base.html**
```html
<!DOCTYPE html>
<html>
<head>
    <title>My Web App</title>
</head>
<body>
    <header>
        <!-- Encabezado -->
    </header>
    <main>
        {% block content %}{% endblock %}
    </main>
    <footer>
        <!-- Pie de página -->
    </footer>
</body>
</html>
```
**index.html**
```html
{% extends "base.html" %}

{% block content %}
    <h1>Bienvenido a mi aplicación web!</h1>
    <p>Este es el contenido de la página de inicio.</p>
{% endblock %}
```
**header.html**
```html
<h1>Bienvenido!</h1>
```
**footer.html**
```html
<p>Copyright 2023</p>
```

Espero que este capítulo te haya proporcionado una comprensión clara de la herencia de templates en Django. En el próximo capítulo, exploraremos cómo utilizar formularios en Django para recopilar datos de nuestros usuarios.