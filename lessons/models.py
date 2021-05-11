from django.db import models
from ckeditor.fields import RichTextField
from course.models import Course


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, default=1)
    order = models.IntegerField()
    title = models.CharField(max_length=127)
    motivation = models.TextField(default='motivation is here')
    refreshment = models.TextField(default='ferreshment is here')
    reflection = models.TextField(default='reflection is here')
    slug = models.SlugField(blank=True)

    def __str__(self):
        return self.title

    def slag(self):
        self.slag = self.title
        self.save()


class lsTag(models.Model):
    tag = models.CharField(max_length=127, blank=True)
    details = models.TextField(blank=True)

    def __str__(self):
        return self.tag


class LessonSegment(models.Model):
    order = models.IntegerField()
    tag = models.ForeignKey(lsTag, on_delete=models.SET_NULL, related_name='tag_set', null=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.SET_NULL, null=True, related_name='ls_set')
    title = models.TextField()
    content = models.TextField()
    hardskill = models.TextField(blank=True)
    softskill = models.TextField(blank=True)

    def __str__(self):
        return self.title


class HomeWork(models.Model):
    order = models.IntegerField(blank=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    title = models.CharField(max_length=127)
    content = models.TextField()

    def __str__(self):
        return self.title

