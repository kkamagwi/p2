from django.urls import path
from django.conf.urls import url

from accounts.views import (
    LoginView,
    MyLogoutView,
    RegisterView,
    guest_email_view,
)
from lessons.views import lesson, lesson_details, lesson_form, lesson_edit

urlpatterns = [
    path('login/', LoginView.as_view(), name='login-page'),
    path('logout/', MyLogoutView.as_view(), name='logout-page'),
    path('register/', RegisterView.as_view(), name='register-page'),
    path('register/email/', guest_email_view, name='guest-email-view'),
  
]
