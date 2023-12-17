"""
URL configuration for goviz project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from goviz1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('homepage/',views.HomePage,name='homepage'),
    path('about/',views.AboutPage,name='about'),
    path('logout/',views.LogoutPage,name='logout'),
    path('contact/',views.Contact,name='contact'),
    path('sorting/',views.SortingPage,name='sorting'),
    path('selectionsort/',views.SelectionSort,name='selectionsort'),
    path('insertionsort/',views.InsertionSort,name='insertionsort'),
    path('quicksort/',views.QuickSort,name='quicksort'),
    path('mergesort/',views.MergeSort,name='mergesort'),
    path('bubblesort/',views.BubbleSort,name='bubblesort'),
    path('heapsort/',views.HeapSort,name='heapsort'),
    path('searching/',views.SearchingPage,name='searching'),
    path('linearsearch/',views.LinearSearch,name='linearsearch'),
    path('binarysearch/',views.BinarySearch,name='binarysearch')
]
