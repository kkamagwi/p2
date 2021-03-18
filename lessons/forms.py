from django import forms
from .models import LessonSegment
from ckeditor.widgets import CKEditorWidget



class LessonSegmentForm(forms.ModelForm):
    class Meta:
        content = forms.CharField(widget=CKEditorWidget())
        model = LessonSegment
        fields = ('order', 'title', 'content')
