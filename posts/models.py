# posts/models.py
from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify

# Create your models here.

# CATEGORY MODELS/TABLE
class Category(models.Model):

	title 	= models.CharField(max_length=150)
	slug 		= models.SlugField(editable=False)

	# Define method to automatically save title as slug
	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		super(Category, self).save(*args, **kwargs)

	def __str__(self):
		return self.title

	# Define method to counting number of posts in each category
	def post_count(self):
		return self.posts.all().count() 


# TAG MODELS/TABLE
class Tag(models.Model):

	title = models.CharField(max_length=50)
	slug  = models.SlugField(editable=False)

	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		super(Tag, self).save(*args, **kwargs)	

	# Define method to counting number of posts in each tag
	def post_count(self):
		return self.posts.all().count() 
		

# POST MODELS/TABLE
class Post(models.Model):

	title 	= models.CharField(max_length=150)
	content 	= models.TextField()
	publishing_date = models.DateTimeField(auto_now_add=True)
	image 	= models.ImageField(blank=True, null=True, upload_to="uploads/")
	user 		= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	slug 		= models.SlugField(default='slug', editable=False)
	category = models.ForeignKey(
					Category, 
					on_delete=models.CASCADE, 
					default=1,
					related_name="posts")
	tag 		= models.ManyToManyField(Tag, related_name="posts", blank=True)
	
	# Define method to automatically save title as slug
	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		super(Post, self).save(*args, **kwargs)

	def __str__(self):
		return self.title