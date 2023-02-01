from django.contrib import admin
from django.urls import path

from todolist.views import (
    FullListView,
    FullListViewOn,
    FullListViewOff,
    ToDoCreateView,
    ToDoDeleteView,
    ToDoUpdateView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('list/', FullListView.as_view(), name='load'),
    path('list/on/', FullListViewOn.as_view(), name='load_on'),
    path('list/off/', FullListViewOff.as_view(), name='load_off'),
    path('add/', ToDoCreateView.as_view(), name='add'),
    path('delete/<int:pk>/', ToDoDeleteView.as_view(), name='delete'),
    path('edit/<int:pk>/', ToDoUpdateView.as_view(), name='edit'),
]
