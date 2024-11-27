from django import forms
from .models import Tag, Task

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']


class TaskForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Task
        fields = ['content', 'deadline', 'tags']