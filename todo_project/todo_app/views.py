from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import TodoData
from .forms import TodoForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView


# Create your views here.
def index(request):
    task2 = TodoData.objects.all()
    if request.method == 'POST':
        task_name = request.POST.get('task')
        task_priority = request.POST.get('priority')
        date2 = request.POST.get('date1')
        desc2 = request.POST.get('desc1')
        task1 = TodoData(name=task_name, priority=task_priority, date=date2, desc=desc2)
        task1.save()
        return redirect('/')

    return render(request, 'home.html', {'task2': task2})


def delete(request, task_id):
    if request.method == 'POST':
        task3 = TodoData.objects.get(id=task_id)
        task3.delete()
        return redirect('/')
    return render(request, 'delete.html')


def updates(request, p_id):
    todo2 = TodoData.objects.get(id=p_id)
    form = TodoForm(request.POST or None, instance=todo2)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'update.html', {'form': form, 'todo2': todo2})


class Tasklistview(ListView):
    model = TodoData
    template_name = 'home.html'
    context_object_name = 'task2'


class Taskdetailview(DetailView):
    model = TodoData
    template_name = 'edit.html'
    context_object_name = 'task22'


class Taskupdateview(UpdateView):
    model = TodoData
    template_name = 'updateview.html'
    context_object_name = 'task22'
    fields = ('name', 'desc', 'priority')

    def get_success_url(self):
        return reverse_lazy('cbvdetail', kwargs={'pk': self.object.id})


class Taskdelete(DeleteView):
    model = TodoData
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvlistview')
