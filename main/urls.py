
from django.urls import path

from main.apps import MainConfig
from main.views import ProductListView, ProductDetailView, ContactCreateView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView, VersionDetailView

app_name = MainConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name = 'home'),
    path('contacts/', ContactCreateView.as_view(), name = 'contacts'),
    path('сreate/', ProductCreateView.as_view(), name='product_create'),
    path('view/<int:pk>/',ProductDetailView.as_view(),name='category_products'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
    #path('activity/<int:pk>/', toggle_activity, name = 'toggle_activity')

    path('view/<int:pk>/', VersionDetailView.as_view(), name='home1'),


]
