from django.contrib import admin
from .models import Lesson, HomeWork, LessonSegment

admin.site.register(Lesson)
admin.site.register(LessonSegment)
admin.site.register(HomeWork)