from django.contrib import admin

from todos.models import Todo


class TodoAdmin(admin.ModelAdmin):
    fields = ('text', 'complete')


admin.site.register(Todo, TodoAdmin)
