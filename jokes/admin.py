from django.contrib import admin
from .models import Joke, Rubric


class JokesAdmin(admin.ModelAdmin):
    list_display = ('content', 'published')
    search_fields = ('content', 'published')


admin.site.register(Joke, JokesAdmin)
admin.site.register(Rubric)
