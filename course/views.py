from django.shortcuts import render
from .models import Course


def course(request):
    courses = Course.objects.all().order_by('order')
    return render(request, 'lessons/lesson.html', 
    {'courses': courses}
    )
