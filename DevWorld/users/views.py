from django.shortcuts import render, redirect
from .models import Profile
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def all_profile(request):
    all_user_profile = Profile.objects.all()
    context = {
        "all_user_profile": all_user_profile
    }
    return render(request, 'users/all_profile.html', context)


def user_profile(request, pk):
    user_profile = Profile.objects.get(id=pk)

    topSkill = user_profile.skill_set.exclude(description__exact="")
    otherSkill = user_profile.skill_set.filter(description="")

    context = {
        "user_profile": user_profile,
        "topSkill": topSkill,
        "otherSkill": otherSkill,
    }
    return render(request, 'users/user_profile.html', context)


def loginUserPage(request):

    if request.user.is_authenticated:
        return redirect('profile')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except :
            messages.error(request, 'Username does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            messages.error(request, 'Username or password is incorrect!')

    return render(request, 'users/login_register.html')


def logoutUserPage(request):
    logout(request)
    messages.success(request, 'User successfully logged out!')
    return redirect('login')