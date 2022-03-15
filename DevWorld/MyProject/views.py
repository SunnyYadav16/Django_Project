from django.shortcuts import render, redirect
from .models import Project
from .forms import MyProjectForm
from django.contrib.auth.decorators import login_required



# Create your views here.
def projects(request):
    myproject = Project.objects.all()
    context = {
        "myproject": myproject,
    }
    return render(request, 'MyProject/HomePage.html', context)


def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    context = {
        "projectObj": projectObj,

    }
    return render(request, 'MyProject/singleProject.html', context)


@login_required(login_url="login")
def create_project(request):
    form = MyProjectForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('projects')
    context = {
        "form": form,
    }
    return render(request, 'MyProject/project_form.html', context)


@login_required(login_url="login")
def update_project(request, pk):
    update_object = Project.objects.get(id=pk)
    form = MyProjectForm(instance=update_object)

    if request.method == 'POST':
        form = MyProjectForm(request.POST, request.FILES or None, instance=update_object)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {
        "form": form,
    }
    return render(request, 'MyProject/project_form.html', context)


@login_required(login_url="login")
def delete_project(request, pk):
    delete_object = Project.objects.get(id=pk)
    if request.method == 'POST':
        delete_object.delete()
        return redirect('projects')
    context = {
        "object": delete_object,
    }
    return render(request, 'MyProject/delete_object.html', context)
