from django.forms import ModelForm

from .models import TodoItem , Workspace

class CreateTodoItem(ModelForm):
    class Meta:
        model = TodoItem
        fields =['label','description']
        
        
class UpdateTodoItem(ModelForm):
    class Meta:
        model = TodoItem
        fields = ['label','description','completed']
        

class CreateWorkspace(ModelForm):
    class Meta:
        model = Workspace
        fields = ['name']