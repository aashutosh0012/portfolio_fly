from django.http import HttpResponse, HttpResponseRedirect	
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import *
#from taggit.models import Tag
from .forms import *

#@login_required decorator: requires user to login before executing functions based views, un-authenticated users will be redirected to login
#Add in settings.py  LOGIN_URL='login/', or in view function @login_required(login_url='login/') 
from django.contrib.auth.decorators import login_required 

#LoginRequiredMixin is class based which requires authentication and un-authenticated users will be redirected to login.
#UserPassesTestMixin tests a function for any custom check, before running the class based view 
#Add in settings.py 	 LOGIN_URL='login/', or in view function @login_required(login_url='login/') 
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin



# class blogHome(ListView):
# 	# Blog Home Page
# 	model = Post
# 	#queryset = Post.objects.all()
# 	ordering = ['-updated']
# 	template_name = 'templates/blogHome.html'
# 	paginate_by = 10

# 	def get_context_data(self, **kwargs):
# 	    context = super(blogHome, self).get_context_data(**kwargs)
# 	    # Pass All Tags as List and its number of tagged Posts
# 	    allTags = Tag.objects.all()
# 	    #allTags = Tag.objects.all().annotate(tag_posts_count=Count('post')).order_by('-tag_posts_count')
# 	    context['allTags'] = allTags
# 	    post_tags = list(value[1] for value in post.tag.values_list())
# 	    print(allTags)
# 	    return context


def tagsListView(request,tag):
	'''Display Posts based on tag filter'''
	# tag = tag.replace('-',' ') #replace '-' from slugify
	print('view=tagsListView')
	if tag == 'all':
		#post_list = Post.objects.all().order_by('-updated')
		post_list = Post.objects.filter(is_approved=True).order_by('-updated')
	else:
		post_list = Post.objects.filter(is_approved=True).filter(tag__name__icontains=tag).order_by('-updated')
	
	template = 'templates/blogHome.html'
	
	# Order Tags List by its number of tagged Posts
	from django.db.models import Count
	allTags = Tag.objects.all().annotate(tag_posts_count=Count('post')).order_by('-tag_posts_count')
	print(f'allTags_list = {allTags}')

	context = {'post_list': post_list,'allTags':allTags,'activeTag':tag}
	return render(request,template,context)


class postDetailView(DetailView):
	print('view=postDetailView')
	model = Post
	template_name = 'templates/postDetail.html'
	def get_context_data(self, **kwargs):
	    context = super(postDetailView, self).get_context_data(**kwargs)
	    post = get_object_or_404(Post, id=self.kwargs['pk'])

	    #Fetch tags of particular Post model & pass to template as list
	    post_tags = list(value[1] for value in post.tag.values_list())
	    context['post_tags'] = post_tags
	    print(f'post_tags= {post_tags}')

	    #Fetch like counts on particular Post model
	    likeCounts = post.LikeCount()
	    context['likes'] = likeCounts

	    liked = False
	    if post.likes.filter(id=self.request.user.id).exists():
	    	liked = True
	    else:
	    	liked = False
	    context['liked'] = liked
	    return context


class createPostView(LoginRequiredMixin, CreateView):
	print('view=createPostView')
	model = Post
	form_class = createPostForm
	template_name = 'templates/createPost.html'
	#fields = '__all__'
	#fields = ('title','body','tag')
	
	#pass logged_in user as author to the Post Model.
	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)


class editPostView(LoginRequiredMixin, UpdateView):
	print('view=editPostView')
	model = Post
	template_name = 'templates/editPost.html'
	#fields = ['title','tag','body']
	form_class = editPostForm


class deletePostView(LoginRequiredMixin, DeleteView):
	print('view=deletePostView')
	model = Post
	template_name = 'templates/deletePost.html'
	success_url = reverse_lazy('blog-home')

#@login_required
def likePostView(request,pk):
	print('view=likePostView')
	# Function to like or unlike a Post.
	post = get_object_or_404(Post, id=request.POST.get('post_id'))
	print("--")
	print('request.POST= ',request.POST.values)
	print('request.POST.get= ',request.POST.get('post_id'))
	print('dir(request.POST)= ',dir(request.POST))
	print("--")
	liked = False
	if post.likes.filter(id=request.user.id).exists():
		post.likes.remove(request.user)
		liked = False
	else:
		post.likes.add(request.user)
		liked = True
	return HttpResponseRedirect(reverse('post-detail', args=[str(pk)]))

	
