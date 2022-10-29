from django.urls import path
from .views import *


urlpatterns = [
	# path('',blogHome.as_view(),name='blog-home'),
	path('',tagsListView,name='blog-home'),
	path('tags/<str:tag>/',tagsListView,name='tag-filter'),
	path('post/<int:pk>',postDetailView.as_view(),name='post-detail'),
	path('createpost/',createPostView.as_view(), name='create-post'),
	path('post/<int:pk>/edit/',editPostView.as_view(), name='edit-post'),
	path('post/<int:pk>/delete',deletePostView.as_view(), name='delete-post'),
	path('like/<int:pk>/',likePostView, name='like-post'),
]
