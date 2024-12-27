from django.db import models

# Create your models here.
## En este archivo se crean clases que representan tablas en la base de datos

## App de proyectos y tareas
class Project(models.Model):
    # definir los campos de la tabla
    name = models.CharField(max_length=200)
    
    # __str__ es un método que devuelve una representación en cadena del objeto
    def __str__(self):
        return self.name


class Task(models.Model):
    ## CharField: campo de texto pequeño
    title = models.CharField(max_length=200)
    ## TextField: campo de texto grande
    description = models.TextField()
    ## ForeignKey: campo que se relaciona con otra tabla
    ## Si eliminamos un proyecto, usamos on_delete=models.CASCADE para eliminar todas las tareas relacionadas en cascada
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    done = models.BooleanField(default=False)
    
    # __str__ es un método que devuelve una representación en cadena del objeto
    def __str__(self):
        return self.title + ' - ' + self.project.name