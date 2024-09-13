**Capítulo 7: Autenticación y Autorización - Sistema de usuarios de Django**

En el capítulo anterior, exploramos la creación de un sistema de usuarios básico en Django. Sin embargo, es importante destacar que esta implementación no es segura ni escalable para proyectos reales. En este capítulo, profundizaremos en el tema de autenticación y autorización en Django, conociendo los detalles del sistema de usuarios y cómo utilizarlo de manera efectiva.

**Configuración inicial**

Antes de empezar a desarrollar nuestro sistema de usuarios, debemos configurar algunas opciones básicas. Primero, instalamos la aplicación `django.contrib.auth`, que es responsable de la autenticación y autorización en Django:
```python
pip install django
```
Luego, agregamos la aplicación al archivo `settings.py` de nuestro proyecto:
```python
INSTALLED_APPS = [
    # ...
    'django.contrib.auth',
    # ...
]
```
Finalmente, creamos una base de datos vacía para nuestra aplicación:
```python
python manage.py migrate
```
**Creación del modelo de usuario**

El sistema de usuarios en Django se basa en un modelo de usuario que hereda de la clase `AbstractUser` de la biblioteca `django.contrib.auth.models`. Para crear nuestro modelo de usuario, creamos una nueva aplicación llamada `users` y luego definimos el modelo:
```python
# users/models.py
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass
```
Luego, creamos una migración para nuestra aplicación `users` y aplicamosla a la base de datos:
```python
python manage.py makemigrations users
python manage.py migrate
```
**Creación del formulario de registro**

Para permitir que los usuarios se registren en nuestro sistema, debemos crear un formulario de registro. Creamos una nueva clase `RegistrationForm` que hereda de la clase `forms.ModelForm`:
```python
# users/forms.py
from django import forms
from .models import User

class RegistrationForm(forms.ModelForm):
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_password2(self):
        # Verificamos que las contraseñas sean iguales
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Las contraseñas no coinciden')
        return password2
```
**Vista de registro**

Para mostrar el formulario de registro en una página, creamos una nueva vista `RegistrationView` que hereda de la clase `FormView`:
```python
# users/views.py
from django.shortcuts import render, redirect
from .forms import RegistrationForm

class RegistrationView(FormView):
    form_class = RegistrationForm
    template_name = 'registration/register.html'

    def form_valid(self, form):
        # Creamos un nuevo usuario con los datos del formulario
        user = User.objects.create_user(
            username=form.cleaned_data['username'],
            email=form.cleaned_data['email'],
            password=form.cleaned_data['password1']
        )
        return redirect('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Registro'
        return context
```
**Plantilla de registro**

Creamos una plantilla `register.html` para mostrar el formulario de registro:
```html
<!-- templates/registration/register.html -->
<h1>{{ title }}</h1>
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Registro</button>
</form>
```
**Vista de login**

Para permitir que los usuarios se autenticen en nuestro sistema, creamos una nueva vista `LoginView` que hereda de la clase `FormView`:
```python
# users/views.py (continuación)
from django.contrib.auth.views import LoginView

class LoginView(LoginView):
    template_name = 'registration/login.html'
```
**Plantilla de login**

Creamos una plantilla `login.html` para mostrar el formulario de login:
```html
<!-- templates/registration/login.html -->
<h1>Iniciar sesión</h1>
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Iniciar sesión</button>
</form>
```
**Autenticación y autorización**

Para autenticar a los usuarios, utilizamos la función `authenticate` de la biblioteca `django.contrib.auth`. Esta función devuelve un objeto `User` o `None` si el usuario no existe:
```python
from django.contrib.auth import authenticate

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Autenticamos al usuario y redirigimos a la página de inicio
            login(request, user)
            return redirect('home')
    return render(request, 'registration/login.html', {'form': LoginForm()})
```
Para autorizar a los usuarios, utilizamos la función `has_perm` de la biblioteca `django.contrib.auth`. Esta función devuelve `True` si el usuario tiene un permiso determinado:
```python
def home_view(request):
    if request.user.has_perm('users.can_view_users'):
        # Mostramos la página de inicio para los usuarios autorizados
        return render(request, 'home.html')
    else:
        # Redirigimos a la página de acceso denegado
        return redirect('access_denied')
```
**Conclusión**

En este capítulo, hemos profundizado en el tema de autenticación y autorización en Django, creando un sistema de usuarios que incluye registro, login y autorización. Aprendimos cómo utilizar las bibliotecas `django.contrib.auth` y `forms` para crear formularios de registro y login, y cómo utilizar las funciones `authenticate` y `has_perm` para autenticar y autorizar a los usuarios.

En el próximo capítulo, exploraremos temas más avanzados de autenticación y autorización en Django, como la creación de perfiles de usuario y la gestión de permisos.