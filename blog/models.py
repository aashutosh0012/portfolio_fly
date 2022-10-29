from django.db import models
from django.contrib.auth.models import User

#taggit package not used
#from taggit.managers import TaggableManager

from django.urls import reverse
from ckeditor.fields import RichTextField


class Tag(models.Model):
	name = models.CharField(max_length=30)
	def __str__(self):
		return self.name

	def tagCount(self):
		'''Returns total like counts on Post model
		Another method as below without adding tagCount() function to class.
		Use annotate in views.py to order tags list by post count.
		allTags = Tag.objects.all().annotate(tag_posts_count=Count('post')).order_by('-tag_posts_count')
		'''
		return Post.objects.filter(tag__name__icontains=self.name).count()

class Post(models.Model):
	title = models.CharField(max_length=200)
	author = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
	summary = RichTextField(blank=True,null=True)	
	body = RichTextField(blank=True,null=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	tag = models.ManyToManyField(Tag, blank=True)
	# tag = TaggableManager()
	likes = models.ManyToManyField(User, related_name='post_likes')
	is_approved = models.BooleanField(default=False)
	
	def __str__(self):
		return self.title

	def get_absolute_url(self):
		print(self.id)
		return reverse('post-detail',kwargs={'pk' : self.pk})  

	def LikeCount(self):
		'''Returns total like counts on Post model'''
		return self.likes.count()
