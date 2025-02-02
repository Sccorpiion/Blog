from django.urls import path
from django.views.generic import TemplateView
from .views import index_view, ToDoListIndex, ToDoListView, ToDoListDoneView, ToDoDetailView

app_name = 'todo_list'

urlpatterns = [
    path('', ToDoListView.as_view(), name='index'),
    # path('', ToDoListIndex.as_view(), name='index')
    # path('', index_view, name='index'),
    path('done/', ToDoListDoneView.as_view(), name='done'),
    path('<int:pk>/detail/', ToDoDetailView.as_view(), name='detail')
]