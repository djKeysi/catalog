import contact as contact
from django.urls import path

from main.apps import MainConfig
from main.views import  contact, StudentListView,StudentCreateView,StudentDetailView,StudentUpdateView

app_name = MainConfig.name


urlpatterns = [
    path('', StudentListView.as_view(), name = 'index'),
    path('contact/', contact, name = 'contact'),
    path('view/<int:pk>/',StudentDetailView.as_view(),name='view_student'),
    path('create/', StudentCreateView.as_view(), name = 'create_student'),
    path('edit/<int:pk>/', StudentUpdateView.as_view(), name = 'update_student')
]
