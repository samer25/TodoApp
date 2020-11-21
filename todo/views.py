from django.shortcuts import render, redirect

# Create your views here.
from django.views.decorators.http import require_POST

from todo.forms import TodoForm
from todo.models import TodoList


def home(req, form=None, form_action='create todo', pk=None):
    if not form:
        form = TodoForm()
    context = {
        'todo': TodoList.objects.all(),
        'todo_form': form,
        'form_action': form_action,
        'pk': pk,
    }
    return render(req, 'index.html', context)


@require_POST
def create_todo(request):
    form = TodoForm(request.POST)

    if form.is_valid():
        todo = TodoList(name=form.cleaned_data['name'], description=form.cleaned_data['description'], is_done=False)
        todo.save()
        return redirect('todos index')

    return home(request, form)


def edit_todo(req, pk):
    todo = TodoList.objects.get(pk=pk)
    if req.method == 'GET':
        form = TodoForm(initial=todo.__dict__)
        return home(req, form, 'edit todo', pk=pk)
    else:
        form = TodoForm(req.POST)
        if form.is_valid():
            todo.name = form.cleaned_data['name']
            todo.description = form.cleaned_data['description']
            todo.save()
        return home(req, form)


@require_POST
def mark_todo_done(req, pk):
    todo = TodoList.objects.get(pk=pk)
    todo.is_done = not todo.is_done
    todo.save()
    return redirect('todos index')


def delete_todo(req):
    pass
