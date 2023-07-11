from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import Persons
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = Persons(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = Persons()
    context = {
        'form': form
    }
    return render(request,'user/register.html',context)

@login_required
def profile(request):
    return render(request,'user/profile.html')