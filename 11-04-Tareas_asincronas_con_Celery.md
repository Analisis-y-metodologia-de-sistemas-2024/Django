**Capítulo 6: Tareas asíncronas con Celery**

En el mundo de la programación, a menudo nos enfrentamos a tareas que requieren un tiempo significativo para ser completadas. Estas tareas pueden incluir procesos de larga duración, como la generación de informes o la envío de correos electrónicos. En Django, podemos utilizar las tareas asíncronas con Celery para ejecutar estas tareas de manera efectiva y eficiente.

**¿Qué es Celery?**

Celery es un framework para el procesamiento en segundo plano que se utiliza ampliamente en el desarrollo web. Fue creado por Ask Solem y se lanzó por primera vez en el año 2007. Celery proporciona una forma sencilla de ejecutar tareas de manera asíncrona, lo que significa que no bloquean la pista principal del servidor. Esto permite a los desarrolladores crear aplicaciones más escalables y eficientes.

**Instalación de Celery**

Para instalar Celery en un proyecto Django, debemos seguir los siguientes pasos:

1. Instalar la biblioteca celery utilizando pip: `pip install celery`
2. Agregar la aplicación celery a nuestro proyecto Django en el archivo `settings.py`: `INSTALLED_APPS = ['django_celery_results', 'celery']`
3. Configurar el broker de Celery en el archivo `settings.py`. El broker es responsable de recibir y enviar las tareas para su procesamiento. Hay varios brokers disponibles, como RabbitMQ, Redis o Amazon SQS.

Ejemplo de configuración del broker:
```
CELERY_BROKER_URL = 'amqp://guest:guest@localhost'
CELERY_RESULT_BACKEND = 'django-db'
```
4. Crear un archivo `tasks.py` en la raíz de nuestro proyecto para definir las tareas que queremos ejecutar.

**Definir Tareas con Celery**

Las tareas en Celery se definen utilizando el decorador `@app.task`. Este decorador indica a Celery que la función que sigue es una tarea que puede ser ejecutada de manera asíncrona.

Ejemplo de una tarea simple:
```
from celery import Celery

app = Celery('tasks', broker='amqp://guest:guest@localhost')

@app.task
def add(x, y):
    return x + y
```
**Ejecutar Tareas con Celery**

Para ejecutar una tarea con Celery, podemos utilizar el método `delay()` o `apply_async()`. El método `delay()` se utiliza cuando queremos ejecutar la tarea de manera asíncrona y recibir el resultado cuando esté disponible. El método `apply_async()` se utiliza cuando queremos ejecutar la tarea de manera asíncronas pero no recibir el resultado.

Ejemplo de ejecución de una tarea con delay():
```
result = add.delay(2, 3)
print(result.get())
```
**Monitorizar Tareas con Celery**

Celery proporciona varias formas de monitorizar las tareas que están en ejecución. Algunas de las opciones disponibles son:

* El administrador de tareas: Es una interfaz web que se puede acceder a través del URL `/admin/celery/task/`. A partir de aquí, podemos ver la lista de tareas que están en ejecución y sus respectivos resultados.
* La consola de Celery: Podemos utilizar la consola de Celery para ver la lista de tareas que están en ejecución y obtener información sobre ellas. Para acceder a la consola de Celery, podemos utilizar el comando `celery -A tasks inspect active`.
* El registro de tareas: Celery también proporciona un registro de tareas que nos permite ver los detalles de las tareas que se han ejecutado anteriormente.

**Ejemplos Prácticos**

En este capítulo, vamos a crear dos ejemplos prácticos que demuestran cómo utilizar Celery para ejecutar tareas asíncronas en un proyecto Django.

### Ejemplo 1: Generación de informes

Supongamos que queremos generar un informe diario que contenga los datos más relevantes del día. Podemos crear una tarea que se encargue de generar este informe y ejecutarla de manera asíncrona utilizando Celery.

Ejemplo de código:
```
from celery import Celery
from datetime import date

app = Celery('tasks', broker='amqp://guest:guest@localhost')

@app.task
def generate_report():
    # Código para generar el informe diario
    report_data = []
    for user in User.objects.all():
        report_data.append({'user': user.name, 'sales': user.sales})
    return report_data

# Ejecutar la tarea de manera asíncrona
report_task = generate_report.delay()
print("Report task has been submitted")
```
### Ejemplo 2: Envío de correos electrónicos

Supongamos que queremos enviar un correo electrónico a todos los usuarios del sistema cada vez que se crea un nuevo registro. Podemos crear una tarea que se encargue de enviar este correo electrónico y ejecutarla de manera asíncrona utilizando Celery.

Ejemplo de código:
```
from celery import Celery
from django.core.mail import send_mail

app = Celery('tasks', broker='amqp://guest:guest@localhost')

@app.task
def send_email(user_id):
    # Código para enviar el correo electrónico
    user = User.objects.get(id=user_id)
    send_mail(subject='Nuevo registro creado', message='Se ha creado un nuevo registro.', from_email='your_email@example.com', recipient_list=[user.email])

# Ejecutar la tarea de manera asíncronas
send_email_task = send_email.delay(1)
print("Email task has been submitted")
```
En resumen, Celery es una herramienta muy útil para ejecutar tareas asíncronas en un proyecto Django. Proporciona una forma sencilla de ejecutar tareas de manera asíncronas y monitorizar su estado. En este capítulo, hemos visto cómo utilizar Celery para definir tareas, ejecutarlas de manera asíncronas y monitorizar su estado. También hemos visto dos ejemplos prácticos que demuestran cómo utilizar Celery en un proyecto Django.

**Conclusión**

En este capítulo, hemos aprendido a utilizar Celery para ejecutar tareas asíncronas en un proyecto Django. Vimos cómo definir tareas con el decorador `@app.task`, ejecutarlas de manera asíncronas utilizando los métodos `delay()` o `apply_async()` y monitorizar su estado utilizando la consola de Celery, el administrador de tareas y el registro de tareas.

En el próximo capítulo, vamos a ver cómo utilizar las señales en Django para notificar a nuestros aplicativos de cambios en el sistema.