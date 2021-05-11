from django.urls import path
from django.conf.urls import url
from .views import lesson, lesson_details, lesson_form, lesson_edit, LessonSegmenUpdate, thematic_plan

app_name = 'lessons'
urlpatterns = [
    path('', lesson),
    path('tp/', thematic_plan, name="thematic_plan"),
    url(r'^(?P<slug>[\w-]+)/$', lesson_details, name="lesson-details"),
    url(r'^add/(?P<slug>[\w-]+)/$', lesson_form, name = "ls-add"),
    # url(r'^edit/(?P<slug>[\w-]+)/(?P<id>[0-9]+)/$', lesson_edit, name='ls-edit'),
    url(r'^(?P<pk>\d+)/update/$', LessonSegmenUpdate.as_view(), name='ls-update'),
]
