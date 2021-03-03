"""platform2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import url

from accounts.views import (
    LoginView,
    MyLogoutView,
    RegisterView,
    guest_email_view,
)
from lessons.views import lesson, lesson_details

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(), name='login-page'),
    path('logout/', MyLogoutView.as_view(), name='logout-page'),
    path('register/', RegisterView.as_view(), name='register-page'),
    path('register/email/', guest_email_view, name='guest-email-view'),
    path('lessons/', lesson),
    url(r'^(?P<slug>[\w-]+)/$', lesson_details, name = "detail"),
]
