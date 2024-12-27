from django.contrib import admin
from .models import Project, Task

# Register your models here.
## Podremos añadir nuestras app al panel de administrador 
admin.site.register(Project)
admin.site.register(Task)