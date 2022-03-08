from django.shortcuts import render
from .models import Profile


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
