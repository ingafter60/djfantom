# posts/views.py
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Post 

# Create your views here.

# class IndexView(TemplateView):
class IndexView(ListView):

	template_name 	= "posts/index.html"
	model = Post
	context_object_name = 'posts'

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super(IndexView, self).get_context_data(**kwargs)
		return context