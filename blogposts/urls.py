from django.urls import path
from blogposts.apps import BlogpostsConfig
from blogposts.views import BlogPostListView, BlogPostCreateView,BlogPostDetailView,BlogPostDeleteView,BlogPostUpdateView

#from blogposts.views import #MaterialCreateView, MaterialListView, MaterialDetailView, MaterialUpdateView, \
    #MaterialDeleteView

app_name = BlogpostsConfig.name

urlpatterns = [
    path('create/', BlogPostCreateView.as_view(), name='create'),
    path('', BlogPostListView.as_view(), name='list'),
    path('view/<int:pk>/', BlogPostDetailView.as_view(), name='view'),
    path('edit/<int:pk>/', BlogPostUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', BlogPostDeleteView.as_view(), name='delete'),

]