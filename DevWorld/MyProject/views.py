from django.shortcuts import render
from .models import Project


# Create your views here.
def projects(request):
    myproject = Project.objects.all()
    context = {
        "myproject": myproject,
    }
    return render(request, 'MyProject/Test.html', context)


def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    context = {
        "projectObj": projectObj,

    }
    return render(request, 'MyProject/singleProject.html', context)


def create_project(request):
    context = {}
    return render(request, 'MyProject/form.html', context)
