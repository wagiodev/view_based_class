from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import New
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView

# Create your views here.

class NewListView(ListView):
    model = New

def new_detail(request, pk):
    new = get_object_or_404(New, pk=pk)
    return render(request, 'new/new_detail.html', {'new': new})

class NewCreate(CreateView):
    model = New
    fields = ['title','description','city','topic']

class NewUpdate(UpdateView):
    model = New
    fields = ['title','description','city','topic']

class NewDelete(DeleteView):
    model = New
    success_url = reverse_lazy('list-news')