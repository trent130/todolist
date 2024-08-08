from django.shortcuts import render, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .forms import todoForm, registerForm
from django.contrib import messages
from .models import TodoItem
from django.contrib.auth.models import User

# Create your views here.
def registerview(request):
    if request.method == "POST":
        form = registerForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            
            if User.objects.filter(email=email).exists():
                messages.error(request, "user email already in use")
                return HttpResponseRedirect(reverse("Todo:register"))
            else:
                messages.success(request, "registration successful")
                login(request, user)
                return HttpResponseRedirect(reverse("Todo:todo_list"))
        else:
            messages.error(request, "invalid form")
    else:        
        form = registerForm()
    context={"title":"register", "form":form}
    return render(request, "registration/register.html", context)
            
@login_required
def todo_list(request):
    if request.method == "POST":
        form = todoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "form has successfully been submitted")
            return  HttpResponseRedirect(reverse("Todo:todo_list"))
        else:
            messages.error(request, "invalid form")
    else:
        form = todoForm()  
    items = TodoItem.objects.all()
    context = {"title":"todo_list", "items":items, "form":form}
    return render(request,"Todo/todo_list.html", context)

@login_required
def todo_details(request, pk):
    item = get_object_or_404(TodoItem, pk=pk)
    context = {"title":"todo details", "item":item}
    return render(request, "Todo/todo_details.html", context)

@login_required
def edit_todo(request, pk):
    item = get_object_or_404(TodoItem, pk=pk)
    if request.method == "POST":
        form = todoForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("Todo:todo_list"))
        else:
            messages.error(request, "invalid input")
            return redirect("Todo:todo_details")
    else:
        form = todoForm(instance=item)
    context = {"title":"edit_todo", "form":form}
    return render(request, "Todo/todo_edit.html", context)

@login_required
def delete_todo(request, pk):
    item = get_object_or_404(TodoItem, pk=pk)
    item.delete()
    return HttpResponseRedirect(reverse("Todo:todo_list")) 