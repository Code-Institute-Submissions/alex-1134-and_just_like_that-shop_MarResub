from django.shortcuts import render

from .models import UserProfile

def profile(request):
    profile = get_object_or_404(UserProfile, user=requestuser)

    template = 'profiles/profile.html'
    context = {
        'profile': profile,
    }

    return render(request, template, context)
