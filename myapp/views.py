from django.shortcuts import render

## la carpeta 'migrations' se llenara a medida que se este trabajando con la base de datos
## Concepto de BDL: las migraciones son una manera de actualizar la BD a partir de codigo de python 

# Create your views here.
## ARCHIVO PRINCIPAL - podemos definir que queremos ejecutar o enviar al cliente o navegador para que se vea en pantalla

# ----------------------------------------------
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render, redirect
from .forms import CreateNewTask, CreateNewProject
# ----------------------------------------------

## Django te pasa el archivo 'request', que contiene información sobre la solicitud que se ha hecho al servidor.
def index(request):
    # return HttpResponse("Index Page")

    title = 'Django Course!!'
    return render(request, 'index.html', {
        'title': title
    })

def about(request):
    # return HttpResponse("About")
    return render(request, 'about.html')

def hello(request, username):
    ## %s es un marcador de posición que se reemplazará por el valor de la variable username
    return HttpResponse("<h1>Hello %s</h1>" % username)

def projects(request):
    # projects = list(Project.objects.values())
    # return JsonResponse(projects, safe=False)
    # return render(request, 'projects/projects.html')

    projects = Project.objects.all()
    return render(request, 'projects/projects.html', {
        'projects': projects
    })

def tasks(request):
# def tasks(request, title):
    
    ## -- Recuperacion desde la BD --
    # task = Task.objects.get(id=id)
    # task = get_object_or_404(Task, title=title)
    # return HttpResponse('task: %s' % task.title)
    tasks = Task.objects.all()
    return render(request, 'tasks/tasks.html', {
        'tasks': tasks
    })


# def create_task(request):
   # print(request.GET['title'])
   # print(request.GET['description'])
   # Task.objects.create(title=request.GET['title'], description=request.GET['description'], project_id=2)
   # return render(request, 'create_task.html', {
   #    'form': CreateNewTask()
   # })

def create_task(request):
    if request.method == 'GET':
        return render(request, 'tasks/create_task.html', {
            'form': CreateNewTask()
        })
    else:
        Task.objects.create(title=request.POST['title'], description=request.POST['description'], project_id=2)
        return redirect('tasks')

def create_project(request):
    if request.method == 'GET':
        return render(request, 'projects/create_project.html', {
            'form': CreateNewProject()
        })
    else:
        Project.objects.create(name=request.POST['name'])
        return redirect('projects')
    
def project_detail(request, id):
    project = get_object_or_404(Project, id=id)
    tasks = Task.objects.filter(project_id=id)
    return render(request, 'projects/project_detail.html', {
        'project': project,
        'tasks': tasks
    })