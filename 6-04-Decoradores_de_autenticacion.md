**Decoradores de Autenticación**

En el capítulo anterior, abordamos la autenticación de usuarios en Django, destacando la importancia de asegurar la integridad de nuestra aplicación web. Ahora, vamos a profundizar en los decoradores de autenticación, una herramienta fundamental para controlar el acceso a nuestras vistas y funcionalidades.

**¿Qué son los decoradores de autenticación?**

Los decoradores de autenticación son funciones que se pueden aplicar a nuestras vistas y funcionalidades para verificar la autenticidad de un usuario antes de permitirle acceder a ciertos recursos. Estos decoradores nos permiten implementar una autorización más estricta, evitando que usuarios no autorizados accedan a información confidencial.

**Cómo funcionan los decorados de autenticación**

Los decoradores de autenticación se basan en la función `@login_required` del paquete `django.contrib.auth.decorators`. Esta función verifica si el usuario actual está autenticado, es decir, si ha iniciado sesión correctamente. Si el usuario no está autenticado, redirige al usuario a la página de inicio de sesión.

**Ejemplo básico**

Supongamos que deseamos crear una vista para mostrar información confidencial solo accesible por usuarios autenticados. Podríamos utilizar el decorador `@login_required` de la siguiente manera:
```python
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def mi_vista(request):
    return render(request, 'mi_template.html', {'mensaje': 'Bienvenido'})
```
En este ejemplo, el decorador `@login_required` se aplica a la función `mi_vista`, lo que significa que solo se permitirá acceder a esta vista si el usuario actual está autenticado.

**Cómo personalizar los decoradores de autenticación**

Aunque el decorador `@login_required` es útil para controlar el acceso a nuestras vistas, podemos personalizarlo para adaptarlo a nuestros necesidades específicas. Por ejemplo, podríamos crear un decorador que verifique si el usuario tiene ciertos permisos antes de permitirle acceder a una vista.
```python
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

@login_required
def mi_vista(request):
    if not request.user.has_perm('mi_app.permiso_especial'):
        raise PermissionDenied
    return render(request, 'mi_template.html', {'mensaje': 'Bienvenido'})
```
En este ejemplo, el decorador `@login_required` se combina con una verificación de permisos para asegurarnos de que solo los usuarios con el permiso `mi_app.permiso_especial` puedan acceder a la vista.

**Otras opciones de autenticación**

Además del decorador `@login_required`, existen otras opciones para implementar la autenticación en Django. Por ejemplo, podemos utilizar el decorador `@user_passes_test` para verificar si un usuario cumple ciertas condiciones antes de permitirle acceder a una vista.
```python
from django.contrib.auth.decorators import user_passes_test

def es_admin(user):
    return user.is_superuser

@admin_required
def mi_vista(request):
    return render(request, 'mi_template.html', {'mensaje': 'Bienvenido'})
```
En este ejemplo, el decorador `@admin_required` se aplica a la función `mi_vista`, lo que significa que solo los administradores del sistema podrán acceder a esta vista.

**Conclusión**

Los decoradores de autenticación son una herramienta poderosa para controlar el acceso a nuestras vistas y funcionalidades en Django. Al combinarlos con otros elementos, como la verificación de permisos y la personalización de la autenticación, podemos crear aplicaciones seguras y escalables. En el siguiente capítulo, exploraremos cómo implementar la autorización en Django, destacando las diferentes opciones y estrategias para controlar el acceso a nuestros recursos.

**Código completo**

A continuación, te proporciono el código completo para los ejemplos presentados en este capítulo:
```python
# mi_app/views.py
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import render

@login_required
def mi_vista(request):
    if not request.user.has_perm('mi_app.permiso_especial'):
        raise PermissionDenied
    return render(request, 'mi_template.html', {'mensaje': 'Bienvenido'})

# mi_app/views.py (continuación)
from django.contrib.auth.decorators import user_passes_test

def es_admin(user):
    return user.is_superuser

@admin_required
def mi_vista_admin(request):
    return render(request, 'mi_template_admin.html', {'mensaje': 'Bienvenido'})
```
Espero que este capítulo haya sido útil para ti. En el próximo capítulo, exploraremos cómo implementar la autorización en Django, destacando las diferentes opciones y estrategias para controlar el acceso a nuestros recursos.