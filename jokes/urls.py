from django.urls import path

from .views import index, by_rubric, JokeCreateView

urlpatterns = [
    path('<int:rubric_id>/', by_rubric, name='by_rubric'),
    path('', index, name='index'),
    path('add/', JokeCreateView.as_view(), name='add'),
]