from django import forms

class CreateNewTask(forms.Form):
    # widget es un atributo que se le asigna a un campo de un formulario para que se renderice de una forma diferente
    title = forms.CharField(label='Titulo de tarea', max_length=200, widget=forms.TextInput(attrs={'class': 'input'}))
    description = forms.CharField(label='Descripcion de la tarea', widget=forms.Textarea(attrs={'class': 'input'}))

class CreateNewProject(forms.Form):
    name = forms.CharField(label='Nombre del proyecto', max_length=200, widget=forms.TextInput(attrs={'class': 'input'}))