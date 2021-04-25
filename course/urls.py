from django.urls import path
from django.conf.urls import url
from .views import course

app_name = 'course'
urlpatterns = [
    path('', course),
    # url(r'^(?P<slug>[\w-]+)/$', lesson_details, name="lesson-details"),
]