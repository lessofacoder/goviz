from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from django.contrib import messages

# Create your views here.

@login_required(login_url='login')

def HomePage(request):
    return render (request,'homepage.html')

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        cpassword=request.POST.get('confirmpassword')
        if password!=cpassword:
            return HttpResponse("!!!Your Password is Not matching!!!")
        else:
            my_user=User.objects.create_user(uname,email,password)
            my_user.save()
            messages.add_message(request, messages.INFO, 'Success')
            return redirect('login')

    return render (request,'index.html')
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def LoginPage(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            username=request.POST.get('username')
            pass1=request.POST.get('password')
            user=authenticate(request,username=username,password=pass1)
            if user is not None:
                login(request,user)
                return redirect('homepage')
            else:
                return HttpResponse("!!!Username or Password was Incorrect!!!")


        return render (request,'login.html')



def LogoutPage(request):
    logout(request)
    return redirect('login')

def AboutPage(request):
    return render (request,'about.html')

def Contact(request):
    return render (request,'code.html')

def SortingPage(request):
    return render (request,'list.html')

def SelectionSort(request):
    return render (request,'ss.html')

def InsertionSort(request):
    return render (request,'is.html')

def QuickSort(request):
    return render (request,'qs.html')

def MergeSort(request):
    return render (request,'ms.html')

def BubbleSort(request):
    return render (request,'bs.html')

def HeapSort(request):
    return render (request,'hs.html')

def SearchingPage(request):
    return render (request,'list2.html')

def LinearSearch(request):
    return render (request,'h_ls.html')

def BinarySearch(request):
    return render (request,'h_bs.html')
