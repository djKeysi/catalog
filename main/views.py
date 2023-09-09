from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView

from main.models import Student


# def home(request):
#     return render(request,'main/home.html')
#
# def contacts(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         phone = request.POST.get('phone')
#         message = request.POST.get('message')
#         print(f'You have new message from {name}({phone}): {message}')
#     return render(request,'main/contacts.html')
class StudentListView(ListView):
    model = Student
    #template_name = 'main/index.html'  # student_detail


class StudentDetailView(DetailView):
    model = Student
    #template_name = 'main/student_detail.html'


class StudentCreateView(CreateView):
    model = Student
    # template_name = 'main/student_form.html'
    fields = ('first_name', 'last_name', 'avatar')
    success_url = reverse_lazy('main:index')

class StudentUpdateView(UpdateView):
    model = Student
    # template_name = 'main/student_form.html'
    fields = ('first_name', 'last_name', 'avatar')
    success_url = reverse_lazy('main:index')


# def home(request):
#     students_list = Student.objects.all()
#     context ={
#         'object_list': students_list,
#         'title':'Главная'
#     }
#     return render(request,'main/home.html',context)

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'You have new message from {name}({phone}): {message}')
    context = {
        'title': 'Контакты'
    }
    return render(request, 'main/contact.html', context)
