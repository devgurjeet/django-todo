from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('addtodo', views.addtodo, name='addtodo'),
    path('complete/<todo_id>', views.complete, name='complete'),
    path('undocomplete/<todo_id>', views.undocomplete, name='undocomplete'),
    path('delete/<todo_id>', views.delete, name='delete'),

]
