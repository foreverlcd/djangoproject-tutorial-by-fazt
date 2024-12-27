"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
## "include" es para incluir otras rutas de urls

## Importamos la vista que creamos en 'myapp/views.py'
# ----------------------------------------------
# Ya no son necesarios estos imports
#from myapp.views import Hello
## Otra forma de importar, pero todo:
#from myapp import views
# ----------------------------------------------
## Podemos esribir las URLS que los usuarios pueden visitar
urlpatterns = [
    path('admin/', admin.site.urls),
    
    ## LAS RUTAS NO DEBEN REPETIRSE!!!
    ## path('ruta', 'nombre de la funcion que se ejecutara')
    ## '' = raiz del proyecto, ruta principal
    ## path('', views.Hello), 
    ## Se cambio la ruta de la vista Hello a 'myapp/views.py' """ <--- Recomendable
    #   path('', Hello),
    #   path('about/', views.About),

    ## Incluimos las rutas de 'myapp/urls.py'
    path('', include('myapp.urls')),   
]
