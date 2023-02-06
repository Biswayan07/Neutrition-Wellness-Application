from django.shortcuts import render
from .forms import *
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .decorators import *
from .filters import foodFilter

def bmi(request):
    return render(request,'bmi.html')

@login_required(login_url='login')
@admin_only
def index(request):
    customers=Customer.objects.all()
    context={'customers':customers}
    return render(request,'main.html',context)


@unauthorized_user
def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            registered = True

        else:
            print(user_form.errors)

    else:
        user_form = UserForm()

    return render(request, 'register.html',
                  {'user_form': user_form, 'registered': registered})

@login_required(login_url='login')
def logut(request):
    logout(request)
    return redirect('login')

@unauthorized_user
def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            messages.info(request,'username or password is invalid')
    return render(request,'login.html')

def addfood(request):
    user=request.user
    cust=user.customer
    if request.method=="POST":
        form =addUserfood(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    form=addUserfood()
    context={'form':form}
    return render(request,'addingfood.html',context)

