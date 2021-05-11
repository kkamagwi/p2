from django.db import models


class Course(models.Model):
    order = models.IntegerField()
    title = models.CharField(max_length=127)
    slug = models.SlugField(blank=True)
    
    def __str__(self):
        return self.title

    def slag(self):
        self.slag = self.title
        self.save()

# TODO календарно тематический
