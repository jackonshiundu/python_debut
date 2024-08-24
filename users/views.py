from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from django.contrib import messages
# Create your views here.
def register(request):
    if request.method =='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Welcome{username}, You are now Logged in')
            return redirect('login')
    else:
        form =RegisterForm()

    return render(request,'user/register.html',{'form':form})

@login_required
def profilepage(request):
    return render(request,'user/profile.html')