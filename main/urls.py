import contact as contact
from django.urls import path

from main.apps import MainConfig
from main.views import home, contact

app_name = MainConfig.name


urlpatterns = [
    path('', home, name = 'index'),
    path('contact/', contact, name = 'contact')
]
