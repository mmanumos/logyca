"""logyca URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from primos.views.views import home, regular_primes, twin_primes, regular_primes_save, twin_primes_save

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('home/', home, name='home'),
    path('regular_primes/<int:quantity>',
         regular_primes, name='regular_primes'),
    path('twin_primes/<int:quantity>',
         twin_primes, name='twin_primes'),
    path('regular_primes_save/<int:quantity>',
         regular_primes_save, name='regular_primes_save'),
    path('twin_primes_save/<int:quantity>',
         twin_primes_save, name='twin_primes_save'),
]
