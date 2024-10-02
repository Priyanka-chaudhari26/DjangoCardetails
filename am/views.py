from django.shortcuts import render,redirect
from .models import Car
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import  SignUpForm

# Create your views here.
def index(request):
    car = Car.objects.all()
    return render(request, 'index.html',{'car': car})

@login_required
def cardetails(request, car_id):
    car = Car.objects.get(id=car_id)
    return render(request, 'cardetails.html', {'car': car})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
    
   
def user_logout(request):
    logout(request)
    return redirect('index')
