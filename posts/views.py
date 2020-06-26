# posts/views.py
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView
from .models import Post, Category 

# Create your views here.

# ALL POSTS
class IndexView(ListView):

	template_name 	= "posts/index.html"
	model = Post
	context_object_name = 'posts'

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super(IndexView, self).get_context_data(**kwargs)
		return context

# SINGLE POST
class PostDetail(DetailView):

	template_name 	= "posts/detail.html"
	model = Post
	context_object_name = 'single'

	def get_context_data(self, **kwargs):
		context = super(PostDetail, self).get_context_data(**kwargs)
		return context

# CATEGORY DETAIL MODELS/TABLE
class CategoryDetail(ListView):

	# Get all posts
	model = Post 
	template_name 	= "categories/category_detail.html"
	context_object_name = 'posts'

	# Define method to get Category with its specific credential (pk)
	def get_queryset(self):
		self.category = get_object_or_404(Category, pk=self.kwargs['pk'])
		# Get all posts based on their category
		return Post.objects.filter(category=self.category).order_by('-id')

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super(CategoryDetail, self).get_context_data(**kwargs)
		self.category = get_object_or_404(Category, pk=self.kwargs['pk'])
		# breadcrumb: home > category_name
		context['category'] = self.category 
		return context