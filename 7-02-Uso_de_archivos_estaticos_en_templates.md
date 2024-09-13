**Capítulo 7: Manejo de Archivos Estáticos y Media**

**Uso de Archivos Estáticos en Templates**

En el capítulo anterior, hemos aprendido a configurar archivos estáticos en Django. Ahora, vamos a profundizar en cómo podemos utilizar estos archivos en nuestros templates para darle vida a nuestras aplicaciones web.

### ¿Qué son los archivos estáticos?

Los archivos estáticos son recursos como imágenes, estilos CSS y scripts JavaScript que no cambian dinámicamente según la aplicación. A diferencia de los archivos dinámicos, que se generan automáticamente en tiempo real, los archivos estáticos se almacenan en un directorio separado y se sirven directamente desde allí.

### ¿Por qué utilizar archivos estáticos en templates?

Los archivos estátics ofrecen varias ventajas cuando se utilizan en nuestros templates:

* **Rendimiento**: Al servir archivos estáticos directamente, podemos evitar la carga adicional de generarlos dinámicamente. Esto puede mejorar significativamente el rendimiento de nuestra aplicación.
* **Flexibilidad**: Los archivos estáticos nos permiten tener control total sobre su contenido y apariencia, lo que es especialmente útil para aplicaciones que requieren una gran cantidad de personalización.
* **Seguridad**: Al no generar los archivos dinámicamente, podemos evitar posibles vulnerabilidades de seguridad relacionadas con la inyección de código.

### Cómo utilizar archivos estáticos en templates

Para utilizar archivos estáticos en nuestros templates, necesitamos seguir los siguientes pasos:

1. **Configuración de archivos estátics**: Primero, debemos configurar el directorio de archivos estáticos en nuestro proyecto Django. Esto se puede hacer editando el archivo `settings.py` y agregando la siguiente línea:
```python
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
```
Donde `BASE_DIR` es el directorio raíz de nuestro proyecto y `static` es el nombre del directorio que contiene los archivos estáticos.

2. **Creación de un template**: A continuación, creamos un nuevo template en nuestro directorio `templates`. Por ejemplo, podemos crear un archivo llamado `index.html` con el siguiente contenido:
```html
<!DOCTYPE html>
<html>
<head>
    <title> Mi aplicación </title>
</head>
<body>
    <h1>¡Bienvenido!</h1>
    <img src="{% static 'imagen.jpg' %}" alt="Imagen">
</body>
</html>
```
Donde `{% static 'imagen.jpg' %}` se utiliza para servir la imagen `imagen.jpg` desde el directorio de archivos estáticos.

3. **Servicio de archivos estáticos**: Para que nuestros archivos estáticos sean servidos correctamente, debemos agregar una ruta en nuestro archivo `urls.py`. Por ejemplo:
```python
from django.conf.urls.static import static

urlpatterns = [
    # ... otras rutas ...
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
```
Donde `settings.STATIC_URL` es la URL base para los archivos estáticos y `settings.STATICFILES_DIRS[0]` es el directorio que contiene los archivos estáticos.

### Ejemplo práctico

Vamos a crear un ejemplo práctico de cómo utilizar archivos estáticos en nuestros templates. Primero, creamos un nuevo directorio llamado `static` dentro del directorio raíz de nuestro proyecto y agrega un archivo llamado `imagen.jpg`.

Luego, editamos el archivo `index.html` para que incluya la imagen:
```html
<!DOCTYPE html>
<html>
<head>
    <title> Mi aplicación </title>
</head>
<body>
    <h1>¡Bienvenido!</h1>
    <img src="{% static 'imagen.jpg' %}" alt="Imagen">
</body>
</html>
```
Finalmente, agregamos la ruta para servir los archivos estáticos en nuestro archivo `urls.py`:
```python
from django.conf.urls.static import static

urlpatterns = [
    # ... otras rutas ...
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
```
Ahora, cuando accedemos a nuestra aplicación web, deberíamos ver la imagen `imagen.jpg` renderizada correctamente en nuestro template.

### Ventajas y desventajas

**Ventajas**:

* Rendimiento mejorado
* Flexibilidad para personalizar el contenido y apariencia
* Seguridad al evitar inyección de código

**Desventajas**:

* Requiere configuración adicional para servir archivos estáticos
* Puede requerir más espacio en disco duro para almacenar los archivos estáticos

En resumen, utilizar archivos estáticos en nuestros templates nos permite tener control total sobre el contenido y apariencia de nuestra aplicación web, mejorar el rendimiento y seguridad. Sin embargo, requiere configuración adicional y puede requerir más espacio en disco duro.

Esperamos que esta sección haya sido útil para aprender cómo utilizar archivos estáticos en nuestros templates con Django. En la siguiente sección, exploraremos cómo manejar archivos multimedia en nuestras aplicaciones web.