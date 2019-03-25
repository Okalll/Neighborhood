from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import SignupForm, HoodForm, UserProfileUpdateForm, UserUpdateForm 
from .models import *
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
@login_required(login_url="/accounts/login/")
def home(request):
    hoods = Hood.objects.all()
    
    return render(request,"home.html",locals())


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.save()
            return render(request, 'home.html')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def new_hood(request):
    current_user = request.user
    if request.method == "POST":
        form = HoodForm(request.POST, request.FILES)
        if form.is_valid():
            hood = form.save(commit=False)
            hood.user = current_user
            hood.save()
        return redirect("home")

    else:
        form = HoodForm()
    return render(request, "new_hood.html", {"form": form})

@login_required
def profile(request):
    """Display user profile information."""
    user = request.user
    return render(request, 'profile.html', {'user': user})

@login_required
def update_profile(request):
    """Edit user profile information."""
    user = request.user
    form1 = UserUpdateForm(instance=user)
    form2 = UserProfileUpdateForm(instance=user.profile)
    if request.method == 'POST':
        form1 = UserUpdateForm(instance=user, data=request.POST)
        form2 = UserProfileUpdateForm(
            instance=user,
            data=request.POST,
            files=request.FILES
        )
        if form1.is_valid() and form2.is_valid():
            form1.save()
            form2.save()
            messages.success(request, "Your profile has been updated!")
            return HttpResponseRedirect(reverse('profile'))
    return render(request, 'update_profile.html',
        {'form1': form1, 'form2': form2})

def details(request, hood_id):
    hoods = Hoods.objects.get(id=hood_id)
    
    return render(request, "details.html", locals())

