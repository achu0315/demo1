from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from todo_app.models import task
from . form import todoform
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView

# Create your views here.

class tasklist(ListView):
    model = task
    template_name = 'index.html'
    context_object_name = 'tas'

class taskdetail(DetailView):
    model = task
    template_name = 'index.html'
    context_object_name = 'tas'

class taskupdate(UpdateView):
    model = task
    template_name = 'update.html'
    context_object_name = 'tas'
    fields = ('name','priority','date')

    def get_success_url(self):
        return reverse_lazy('index.html',kwargs={'pk':self.object.id})

class taskdelete(DeleteView):
    model = task
    template_name = 'delete.html'
    success_url = reverse_lazy('home')

def demo(request):
    tasks = task.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name','')
        priority = request.POST.get('priority','')
        date=request.POST.get('date','')
        todo = task(name=name, priority=priority, date=date)
        todo.save()
    return render(request, 'index.html',{'tas':tasks})


# def detail(request):
#
#     return render(request, 'detail.html', {'tas': tasks})

def delete(request,taskid):
    task1=task.objects.get(id=taskid)
    if request.method=='POST':
        task1.delete()
        return redirect('/')

    return render(request,'delete.html')

def update(request,id):
    up = task.objects.get(id=id)
    upf = todoform(request.POST or None, instance=up)

    if upf.is_valid():
        upf.save()
        return redirect('/')
    return render(request,'update.html',{'up':up,'upf':upf})



