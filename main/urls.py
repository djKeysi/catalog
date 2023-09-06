
from django.urls import path

from main.apps import MainConfig
from main.views import home, contacts, categories, category_products

app_name = MainConfig.name

urlpatterns = [
    path('', home, name = 'home'),
    path('contacts/', contacts, name = 'contacts'),
    path('categories/', categories, name = 'categories'),
    path('<int:pk>/products/', category_products, name = 'category_products')
]
