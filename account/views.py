from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, RegisterForm


class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super(RegisterView, self).form_valid(form)


class UserLogin(LoginView):
    form_class = LoginForm
    template_name = 'login.html'

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse('index')


def user_logout(request):
    logout(request)
    return redirect('index')
