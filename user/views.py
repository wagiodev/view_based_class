from django.shortcuts import render
from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from .form import  LoginForm

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            auth_login(request, user)
            return redirect('saludo')
    return render(request, 'login.html')

from django.views import View
class LoginFormView(View):
    form_class = LoginForm
    initial = {}
    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                auth_login(request, user)
                return redirect('saludo')
            return redirect('saludo')

        return render(request, self.template_name, {'form': form})


def logout(request):
    auth_logout(request)
    return redirect('saludo')

def saludo(request):
    return render(request, 'saludo.html')

@login_required(login_url='/user/login/')
def info(request):
    return render(request, 'info.html')


from django.views.generic import ListView
from django.contrib.auth.models import User

class UserListView(ListView):
    model = User