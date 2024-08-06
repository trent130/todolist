from django import forms
from .models import TodoItem

class todoForm(forms.ModelForm):
    
    class Meta:
        model = TodoItem
        fields = ("title", "description", "due_date", "completed")
        
        widgets = {
            "title": forms.TextInput(attrs={"class":"form-control", "placeholder":"Enter your title here"}),
            "description": forms.Textarea(attrs={"class":"form-control", "placeholder":"Add a new task...", "rows":5}),
            "due_date": forms.DateInput(attrs={"class":"form-control", "type":"date"}),
            "completed": forms.CheckboxInput(attrs={"class":"form-check-input",}),
        }