from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .forms import JokeForm

from .models import Joke, Rubric


def index(req):
    jokes = Joke.objects.order_by('-published')

    rubrics = Rubric.objects.all()
    context = {'jokes': jokes, 'rubrics': rubrics}
    return render(req, 'jokes/index.html', context)


def by_rubric(req, rubric_id):
    jokes = Joke.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {'jokes': jokes, 'rubrics': rubrics, 'current_rubric': current_rubric}
    return render(req, 'jokes/by_rubric.html', context)


class JokeCreateView(CreateView):
    template_name = 'jokes/create.html'
    form_class = JokeForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context

