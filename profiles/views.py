from django.shortcuts import render, redirect
from profiles.models import Profile
from profiles.forms import ProfileForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def profile_view(request):
    profile = Profile.objects.get(user=request.user)
    form = ProfileForm(request.POST or None, request.FIELS or None)
    confirm = True

    if form.is_valid():
        form.save()
        confirm = True

    ctx = {
        'profile': profile,
        'form': form,
        'confirm': confirm
    }

    return render(request, 'profiles/main.html', ctx)

@login_required
def add_order_view(request):
    pass

@login_required
def list_order_view(request):
    pass

@login_required
def update_order_view(request, **kwargs):
    pass

@login_required
def delete_order_view(request, **kwargs):
    pass



