
from django.urls import path

from main.apps import MainConfig
from main.views import  ProductListView,ProductDetailView,ContactCreateView

app_name = MainConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name = 'home'),
    path('contacts/', ContactCreateView.as_view(), name = 'contacts'),
    #path('categories/', categories, name = 'categories'),
    #path('<int:pk>/products/', CategoryListView.as_view(), name = 'category_products')
    #path('view/<int:pk>/', ProductCreateView.as_view(), name='category_products'),
    path('view/<int:pk>/',ProductDetailView.as_view(),name='category_products'),
    #path(r'^post/(?P<pk>\d+)/$', PostView.as_view(),name = 'contacts')
]
