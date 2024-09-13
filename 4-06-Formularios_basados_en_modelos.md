**Capítulo 9: Templates y Formularios - Formularios Basados en Modelos**

Django proporciona una forma sencilla de crear formularios en los que se pueden incluir campos dinámicos a través del uso de modelos. Los formularios basados en modelos son un tipo de formulario que se crea automáticamente a partir de un modelo de Django. Esto permite a los desarrolladores enfocarse en la lógica de negocio sin preocuparse por la creación y manejo de los campos del formulario.

**Ventajas de los Formularios Basados en Modelos**

Los formularios basados en modelos tienen varias ventajas. Algunas de las más importantes son:

* **Facilitan la creación de formularios complejos**: Los formularios basados en modelos pueden incluir campos dinámicos, lo que facilita la creación de formularios complejos con múltiples campos y validaciones.
* **Reducen el código**: Al crear un formulario a partir de un modelo, se reduce significativamente el código que debe escribirse. Esto hace que sea más fácil mantener y actualizar los formularios.
* **Mejoran la seguridad**: Los formularios basados en modelos pueden incluir validaciones y autenticación automáticamente, lo que mejora la seguridad del sistema.

**Creación de un Formulario Basado en Modelo**

Para crear un formulario basado en modelo, se debe seguir los siguientes pasos:

1. **Crear un modelo**: Primero, se debe crear el modelo que se va a utilizar para crear el formulario. Esto se hace mediante la creación de una clase que hereda de `models.Model`.
2. **Crear un formulario**: Luego, se debe crear el formulario utilizando la función `forms.ModelForm`. Esta función toma como parámetro el nombre del modelo y devuelve un objeto de tipo `ModelForm`.
3. **Definir los campos**: Los campos del formulario se definen mediante la atribución de una lista de campos al atributo `fields` del objeto de formulario.
4. **Crear la vista**: Finalmente, se debe crear la vista que manejará las solicitudes y respuestas relacionadas con el formulario.

**Ejemplo de Creación de un Formulario Basado en Modelo**

A continuación, se muestra un ejemplo de creación de un formulario basado en modelo:
```python
# models.py
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

# forms.py
from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('name', 'email')
```
En este ejemplo, se crea un modelo `User` con campos `name` y `email`. Luego, se crea un formulario `UserForm` que hereda de `ModelForm` y se define el campo `fields` para incluir los campos `name` y `email`.

**Uso del Formulario en una Vista**

Una vez creado el formulario, se puede utilizar en una vista para manejar las solicitudes y respuestas relacionadas con el formulario. A continuación, se muestra un ejemplo de creación de una vista que utiliza el formulario:
```python
# views.py
from django.shortcuts import render
from .forms import UserForm

def user_create_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm()

    return render(request, 'user_form.html', {'form': form})
```
En este ejemplo, se crea una vista `user_create_view` que maneja las solicitudes y respuestas relacionadas con el formulario. La vista utiliza la función `is_valid()` para validar los datos del formulario y, si son válidos, se guarda en la base de datos utilizando la función `save()`.

**Templating**

Finalmente, se puede utilizar el formulario en un template para mostrar los campos y permitir al usuario completarlos. A continuación, se muestra un ejemplo de creación de un template que utiliza el formulario:
```html
<!-- user_form.html -->
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Crear usuario</button>
</form>
```
En este ejemplo, se utiliza la función `as_p` para mostrar los campos del formulario en un formato de parágrafo.

**Conclusión**

Los formularios basados en modelos son una forma eficiente y segura de crear formularios dinámicos en Django. Algunas de las ventajas de usar formularios basados en modelos incluyen la facilitación de la creación de formularios complejos, la reducción del código y la mejora de la seguridad. En este capítulo, se ha visto cómo crear un formulario basado en modelo y utilizarlo en una vista para manejar las solicitudes y respuestas relacionadas con el formulario.

**Revisión de los Conceptos**

* Formularios basados en modelos: son formularios que se crean automáticamente a partir de un modelo de Django.
* Ventajas de los formularios basados en modelos: facilitan la creación de formularios complejos, reducen el código y mejoran la seguridad.
* Creación de un formulario basado en modelo: se crea un modelo, luego se crea un formulario utilizando la función `forms.ModelForm` y se definen los campos del formulario.
* Uso del formulario en una vista: se utiliza el formulario en una vista para manejar las solicitudes y respuestas relacionadas con el formulario.

**Ejercicios**

1. Cree un modelo de usuario que tenga campos para nombre, email y contraseña.
2. Cree un formulario basado en modelo para el modelo de usuario.
3. Utilice el formulario en una vista para crear un nuevo usuario.
4. Modifique la vista para validar los datos del formulario antes de guardarlos en la base de datos.
5. Crea un template que muestre los campos del formulario y permita al usuario completarlos.