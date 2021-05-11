from django.contrib import admin
from .models import Lesson, HomeWork, LessonSegment, lsTag

admin.site.register(Lesson)
admin.site.register(LessonSegment)
admin.site.register(HomeWork)
admin.site.register(lsTag)