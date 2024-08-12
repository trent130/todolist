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
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Enter your password"}), max_length=150)
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Confirm your password"}), max_length=150, label="Confirm Password")
    
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
    
    widgets = {
        "username": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter your username"}),
        "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Enter your email"}),
        
    }

    def clean_password(self):
        cleaned_data = self.cleaned_data
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match")
        return password2
            