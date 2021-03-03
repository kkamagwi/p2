from django.shortcuts import render
from .models import Lesson, LessonSegment, HomeWork

def lesson(request):
    lessons = Lesson.objects.all()
    return render(request, 'lessons/lesson.html', 
    {'lessons': lessons}
    )

def lesson_details(request, slug):
    lessons = Lesson.objects.get(slug=slug)
    ls = LessonSegment.objects.filter(lesson=lessons.id).order_by('order')
    hw = HomeWork.objects.filter(lesson=lessons.id).order_by('order')
    return render(request, 'lessons/lesson_detail.html', {'lesson': lessons, 'ls':ls, 'hw': hw})
