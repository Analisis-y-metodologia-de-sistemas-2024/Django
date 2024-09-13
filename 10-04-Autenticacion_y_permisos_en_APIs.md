**Capítulo 6: Autenticación y permisos en APIs**

En el capítulo anterior, exploramos las bases de Django REST Framework y cómo crear API utilizando serializadores y vistas basadas en clases. Sin embargo, una API no es segura si no se autentica y controla los permisos. En este capítulo, profundizaremos en la autenticación y permisos en APIs de Django.

**Qué es la autenticación**

La autenticación es el proceso de verificar la identidad de un usuario o entidad que intenta acceder a una API. La autenticación se puede realizar utilizando credenciales como usuarios y contraseñas, token de acceso, certificados SSL/TLS, entre otros.

En Django REST Framework, existen varias formas de autenticar a los usuarios. Una de las más comunes es utilizar el sistema de autenticaciónbuiltin que viene con Django.

**Autenticación básica**

Para habilitar la autenticación en una vista API, debemos configurar la clase `APIView` y especificar un método de autenticación. Por defecto, Django REST Framework utiliza el método `BasicAuthentication`, que verifica la credencial del usuario mediante la función `authenticate`.

A continuación, te mostramos un ejemplo de cómo habilitar la autenticación básica en una vista API:
```python
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

class MyView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({'message': 'Hello, authenticated user!'})
```
En este ejemplo, la vista `MyView` solo se puede acceder si el usuario está autenticado. Si un usuario intenta acceder a esta vista sin estar autenticado, Django REST Framework devolverá un error de autenticación.

**Token-based authentication**

Otra forma común de autenticar a los usuarios es utilizar tokens. Un token es una cadena de texto que se genera cuando un usuario se autentica correctamente y se envía en la cabecera HTTP `Authorization`.

En Django REST Framework, podemos habilitar la autenticación con tokens utilizando el mixin `TokenAuthentication`. Para hacerlo, debemos configurar la clase `APIView` y especificar el mixin de autenticación.

A continuación, te mostramos un ejemplo de cómo habilitar la autenticación con tokens en una vista API:
```python
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication

class MyView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({'message': 'Hello, authenticated user!'})
```
En este ejemplo, la vista `MyView` solo se puede acceder si el usuario está autenticado con un token válido. Si un usuario intenta acceder a esta vista sin estar autenticado, Django REST Framework devolverá un error de autenticación.

**Permisos**

Una vez que los usuarios están autenticados, es importante controlar qué acciones pueden realizar en la API. Los permisos son una forma de controlar quiénes pueden realizar qué acciones en la API.

En Django REST Framework, podemos definir permisos utilizando el mixin `Permission`. Para hacerlo, debemos crear un archivo de configuración que contenga las reglas de permiso y luego especificar estas reglas en nuestra vista API.

A continuación, te mostramos un ejemplo de cómo definir un permiso y aplicarlo a una vista API:
```python
from rest_framework.permissions import IsAuthenticated, Permission
from rest_framework.response import Response
from rest_framework.views import APIView

class MyPermission(Permission):
    def has_permission(self, request, view):
        return request.user.is_superuser

class MyView(APIView):
    permission_classes = [IsAuthenticated, MyPermission]

    def get(self, request):
        return Response({'message': 'Hello, authenticated user!'})
```
En este ejemplo, la vista `MyView` solo se puede acceder si el usuario está autenticado y tiene permiso para hacerlo. Si un usuario intenta acceder a esta vista sin estar autenticado o sin tener permiso, Django REST Framework devolverá un error de permiso.

**Autenticación y permisos en la práctica**

A continuación, te mostramos un ejemplo de cómo utilizar la autenticación y permisos en una aplicación real:

Supongamos que estamos creando una API para un sistema de gestión de proyectos. La API debe ser accesible solo por los usuarios autorizados y deben tener permiso para realizar ciertas acciones.

 Primero, creamos un archivo de configuración `permissions.py` que contiene las reglas de permiso:
```python
from rest_framework.permissions import IsAuthenticated

class ProjectPermission(Permission):
    def has_permission(self, request, view):
        return request.user.is_superuser or request.user.has_perm('project.add_project')

class UserPermission(Permission):
    def has_permission(self, request, view):
        return request.user.is_superuser or request.user.has_perm('user.change_user')
```
Luego, creamos una vista API que utiliza estos permisos:
```python
from rest_framework.response import Response
from rest_framework.views import APIView

class ProjectView(APIView):
    permission_classes = [IsAuthenticated, ProjectPermission]

    def get(self, request):
        return Response({'message': 'Hello, authenticated user!'})

class UserView(APIView):
    permission_classes = [IsAuthenticated, UserPermission]

    def get(self, request):
        return Response({'message': 'Hello, authenticated user!'})
```
Finalmente, en nuestra aplicación principal `urls.py`, especificamos las vistas API y habilitamos la autenticación:
```python
from django.urls import path
from rest_framework import routers
from .views import ProjectView, UserView

router = routers.DefaultRouter()
router.register(r'projects', ProjectView)
router.register(r'users', UserView)

urlpatterns = [
    path('', include(router.urls)),
]
```
En este ejemplo, la API es accesible solo por los usuarios autorizados y deben tener permiso para realizar ciertas acciones. La autenticación se realiza utilizando tokens y los permisos se definen en el archivo de configuración `permissions.py`.

**Conclusión**

En este capítulo, hemos explorado la autenticación y permisos en APIs de Django REST Framework. Vimos cómo habilitar la autenticación básica y token-based, así como cómo definir permisos utilizando mixin `Permission`. También vimos un ejemplo práctico de cómo utilizar la autenticación y permisos en una aplicación real.

En el próximo capítulo, exploraremos cómo crear APIs que utilizan datos desde bases de datos relacionales y no relacionales.