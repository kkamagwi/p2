from django.db import models



class Lesson(models.Model):
    order = models.IntegerField()
    title = models.CharField(max_length=127)
    exersises = models.TextField(blank=True)
    slug = models.SlugField(blank=True)

    def __str__(self):
        return self.title

    def slag(self):
        self.slag = self.title
        self.save()


class LessonSegment(models.Model):
    order = models.IntegerField()
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    title = models.TextField()
    content = models.TextField()

    def __str__(self):
        return self.title

class HomeWork(models.Model):
    order = models.IntegerField(blank=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    title = models.CharField(max_length=127)
    content = models.TextField()

    def __str__(self):
        return self.title