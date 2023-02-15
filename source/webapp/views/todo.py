from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.edit import UpdateView, DeleteView

from webapp.models import ToDo


class AddView(View):
    def get(self, request: WSGIRequest):
        return render(request, 'todo_create.html')

    def post(self, request: WSGIRequest):
        todo_data = {
            'title': request.POST.get('title'),
            'description': request.POST.get('description'),
            'status': request.POST.get('status'),
            'completion_at': request.POST.get('completion_at'),
            'detailed_description': request.POST.get('detailed_description')
        }
        todo = ToDo.objects.create(**todo_data)
        return redirect(f'/todo/?pk={todo.pk}')


class DetailView(View):
    def get(self, request: WSGIRequest):
        todo_pk = request.GET.get('pk')
        todo = ToDo.objects.get(pk=todo_pk)
        context = {'todo': todo}
        return render(request, 'todo.html', context=context)


class ToDoUpdateView(UpdateView):
    model = ToDo
    template_name = 'update_todo.html'
    fields = [
        "title",
        "description",
        "status",
        "completion_at",
        'detailed_description'
    ]
    success_url = "/"


class ToDoDeleteView(DeleteView):
    model = ToDo
    success_url = '/'
    template_name = "todo.html"
