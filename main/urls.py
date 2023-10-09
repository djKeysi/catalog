from django.urls import path
from django.views.decorators.cache import cache_page

from main.apps import MainConfig
from main.views import ProductListView, ProductDetailView, ContactCreateView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView

app_name = MainConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', ContactCreateView.as_view(), name='contacts'),
    path('сreate/', ProductCreateView.as_view(), name='product_create'),
    path('view/<int:pk>/',cache_page(60)(ProductDetailView.as_view()), name='category_products'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),

]
