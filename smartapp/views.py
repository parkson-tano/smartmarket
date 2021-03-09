from django.shortcuts import render
from django.http import  HttpResponse
from django.views.generic import CreateView, TemplateView
from .forms import *
from django.urls import reverse_lazy, reverse
# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["custom"] = Customer.objects.all()
        return context
    

class CustomerRegisistraionView(CreateView):
    template_name = 'register.html'
    form_class = CustomerRegistrationForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        email = form.cleaned_data.get('email')
        user = User.objects.create_user(username, email, password)
        form.instance.user = user
        return super().form_valid(form)