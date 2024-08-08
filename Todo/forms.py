from django import forms
from .models import TodoItem
from django.contrib.auth.models import User

class todoForm(forms.ModelForm):
    
    class Meta:
        model = TodoItem
        fields = ("title", "description", "due_date", "completed")
        labels = {
            "title": "Title",
            "description": "Description",
            "due_date": "Due_date",
            "completed": "Completed",
        }
        
        widgets = {
            "title": forms.TextInput(attrs={"class":"form-control", "placeholder":"Enter your title here"}),
            "description": forms.Textarea(attrs={"class":"form-control", "placeholder":"Add a new task...", "rows":5}),
            "due_date": forms.DateInput(attrs={"class":"form-control", "type":"date"}),
            "completed": forms.CheckboxInput(attrs={"class":"form-check-input",}),
        }

class registerForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput(), max_length=150)
    password = forms.CharField(widget=forms.PasswordInput(), max_length=150)
    
    class Meta:
        model = User
        fields = ["username", "email", "password", "password1"]
            