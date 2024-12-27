from django.urls import path
from . import views

## Si el proyecto es grande, lo recomendable es tener otro archivo de rutas de urls para cada app
    
urlpatterns = [
    path('', views.index, name='index'), # name='index' es un nombre que se le asigna a la ruta
    path('about/', views.about, name='about'),    
    # path('hello/<str:name>/', views.Hello), # Se puede especificar el tipo de dato que se espera    
    path('hello/<str:username>', views.hello, name='hello'),
    path('projects/', views.projects, name='projects'),
    path('projects/<int:id>', views.project_detail, name='project_detail'),
    # path('tasks/<str:title>', views.tasks)
    path('tasks/', views.tasks, name='tasks'),
    path('create_task/', views.create_task, name='create_task'),
    path('create_project/', views.create_project, name='create_project'),
]
