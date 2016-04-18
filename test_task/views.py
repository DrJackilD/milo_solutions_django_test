import csv
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .models import CustomUserModel as User
from .templatetags import custom_tags
from .forms import UserForm, EditUserForm, LoginForm


def list_of_users(request):
    all_users = User.objects.all()
    context = {'users': all_users}
    return render(request, 'test_task/list.html', context=context)


def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            user = User.objects.get(('username', request.POST['username']))
            user.set_password(request.POST['password'])
            user.save()
            return redirect(list_of_users)
    else:
        form = UserForm()
    return render(request, 'test_task/register.html', {'form': form})


@login_required(login_url='/login')
def edit_user(request):
    if request.method == 'POST':
        form = EditUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect(list_of_users)
    else:
        form = EditUserForm(instance=request.user)
    return render(request, 'test_task/edit.html', {'form': form})


def view_user(request):
    return render(request, 'test_task/view.html')


def log_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect(list_of_users)
    form = LoginForm()
    return render(request, 'test_task/login.html', {'form': form})


def download_list(request):
    users = User.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="list_of_all_users.csv"'

    writer = csv.writer(response)
    writer.writerows([[user.username, user.date_of_birth, custom_tags.eligible(user.date_of_birth),
                       user.random_int, custom_tags.bizz_fuzz(user.random_int)]
                      for user in users])
    return response
