from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView


# Create your views here.

#def index(request):
#    return HttpResponse("Hello, World. You're ath flag index.")

class HomePageView(TemplateView):
    template_name = 'index.html'

