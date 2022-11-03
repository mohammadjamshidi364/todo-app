from django.forms import ModelForm

from .models import TodoItem

class CreateTodoItem(ModelForm):
    class Meta:
        model = TodoItem
        fields =['label','description']
        
        
class UpdateTodoItem(ModelForm):
    class Meta:
        model = TodoItem
        fields = "__all__"
        