from django.shortcuts import render
from .models import Lesson, LessonSegment, HomeWork
from .forms import LessonSegmentForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView


def index(request):
    return render(request, 'index.html', )

def lesson(request):
    lessons = Lesson.objects.all().order_by('order')
    return render(request, 'lessons/lesson.html', 
    {'lessons': lessons}
    )

def lesson_details(request, slug):
    lessons = Lesson.objects.get(slug=slug)
    ls = LessonSegment.objects.filter(lesson=lessons.id).order_by('order')
    hw = HomeWork.objects.filter(lesson=lessons.id).order_by('order')
    return render(request, 'lessons/lesson_detail.html', {'lesson': lessons, 'ls':ls, 'hw': hw})


def lesson_form(request, slug):
    lesson = Lesson.objects.get(slug=slug)
    lessons = Lesson.objects.filter(slug=slug)
    form = LessonSegmentForm(request.POST)
    ls = LessonSegment.objects.filter(lesson=lesson.id).order_by('order')
    if form.is_valid():
        lesson = form.save(commit=False)
        lesson.save()
        return redirect('lessons:ls-add')
    return render(request, 'lessons/lesson_form.html', {'lessons': lessons, 'form': form, 'ls': ls})


# class LessonSegmentCreate(CreateView):
    # lesson = Lesson.objects.get(slug=slug)
#     model = LessonSegment.objects.filter(lesson=lesson.id, id=id)
#     fields = '__all__'
    
class LessonSegmenUpdate(UpdateView):
    model = LessonSegment
    fields = ['order','lesson','title','content']
    success_url = 'lessons'

# class LessonSegmenDelete(DeleteView):
#     model = Author
#     success_url = reverse_lazy('authors')

def lesson_edit(request, id, slug):
    lessons = Lesson.objects.get(slug=slug)
    try:
        ls = LessonSegment.objects.filter(lesson=lessons.id, id=id)
 
        if request.method == "POST":
            ls.order = request.POST.get("order")
            ls.title = request.POST.get("title")
            ls.content = request.POST.get("content")
            ls.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, 'lessons/edit_lesson_form.html', {"ls": ls})
    except LessonSegment.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")

def lesson_segment_delete(request, id):
    try:
        lessons = LessonSegmentForm.objects.get(id=id)
        lesson.delete()
        return HttpResponseRedirect("/")
    except LessonSegment.DoesNotExist:
        return HttpResponseNotFound("<h2>Lesson Segment not found</h2>")