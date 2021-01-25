from django import forms

from .models import Joke, Rubric


class JokeForm(forms.ModelForm):
    class Meta:
        model = Joke
        fields = ('content', 'rubric')
        labels = {'rubric': 'Рубрики'}
        widgets = {'rubric': forms.CheckboxSelectMultiple()}
