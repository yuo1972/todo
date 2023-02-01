from django.views.generic import (
    CreateView,
    ListView,
    DeleteView,
    UpdateView,
)
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse_lazy

from .models import ToDo


class FullListView(ListView):
    context_object_name = "todo_"
    queryset = ToDo.objects.all()
    template_name = "todo_list.html"


class FullListViewOn(ListView):
    context_object_name = "todo_"
    queryset = ToDo.objects.filter(is_done=True)
    template_name = "todo_list_on.html"


class FullListViewOff(ListView):
    context_object_name = "todo_"
    queryset = ToDo.objects.filter(is_done=False)
    template_name = "todo_list_off.html"


class ToDoCreateView(CreateView):
    model = ToDo
    fields = ["name", "is_done"]
    template_name = "todo_create.html"
    success_url = "/list/"


class ToDoDeleteView(DeleteView):
    model = ToDo
    template_name = "todo_delete.html"
    success_url = reverse_lazy("load")


class ToDoUpdateView(UpdateView):
    model = ToDo
    fields = ["name", "is_done"]
    template_name = "todo_edit.html"
    success_url = reverse_lazy("load")
