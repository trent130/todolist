from django.shortcuts import render, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from Todo.forms import todoForm, registerForm, userprofileForm
from django.contrib import messages
from .models import TodoItem,UserProfile
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View


# Create your views here.
def registerview(request):
    if request.method == "POST":
        form = registerForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            
            if User.objects.filter(email=email).exists():
                messages.error(request, "User email already in use")
                return HttpResponseRedirect(reverse("Todo:register"))
            
            user = form.save(commit=False)  # Don't save yet
            user.set_password(form.cleaned_data["password1"])  # Set the password
            user.save()  # Now save the user
            messages.success(request, "Registration successful")
            login(request, user)  # Log the user in
            return HttpResponseRedirect(reverse("Todo:todo_list"))
        else:
            messages.error(request, "Invalid form")
    else:        
        form = registerForm()
    context = {"title": "Register", "form": form}
    return render(request, "registration/register.html", context)

            
@login_required
def todo_list(request):
    if request.method == "POST":
        form = todoForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            messages.success(request, "form has successfully been submitted")
            return  HttpResponseRedirect(reverse("Todo:todo_list"))
        else:
            messages.error(request, "invalid form")
    else:
        form = todoForm()  
    items = TodoItem.objects.filter(completed=False, user=request.user)
    completed_items = TodoItem.objects.filter(completed=True, user=request.user)
    context = {"title":"todo_list", "items":items, "form":form, "completed_items":completed_items}
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

@login_required
def delete_all_todo(request):
    delete_items = TodoItem.objects.all()
    delete_items.clear()
    return HttpResponseRedirect(reverse("Todo:todo_list"))

class UserProfileView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user_profile, created = UserProfile.objects.get_or_create(user=request.user)
        form = userprofileForm(instance=user_profile)
        
        context = {'user_profile': user_profile, 'form': form}
        return render(request, "Todo/userprofile.html", context)
    
    def post(self, request, *args, **kwargs):
        user_profile, created = UserProfile.objects.get_or_create(user=request.user)
        form = userprofileForm(request.POST, request.FILES, instance=user_profile)
        
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile has been updated")
            return HttpResponseRedirect(reverse("Todo:user_profile"))
        
        context = {'user_profile': user_profile, 'form': form}
        return render(request, "Todo/userprofile.html", context)

    