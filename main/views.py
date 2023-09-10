from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

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

class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('main:index')

def toggle_activity(request,pk):
    student_item=get_object_or_404(Student,pk=pk)
    if student_item.is_active:
        student_item.is_active = False
    else:
        student_item.is_active = True
    student_item.save()
    return redirect(reverse('main:index'))


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
