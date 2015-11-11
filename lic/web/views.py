from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, DetailView
from django.views.generic import View
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.


class HomeView(TemplateView):

    template_name = "home.html"

class Login(View):

    def post(self, request):

        username = request.POST['username']
        password = request.POST['password']
        print "username = ", username
        print "password = ", password
        return HttpResponseRedirect("/")
