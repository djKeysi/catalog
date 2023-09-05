from django.shortcuts import render

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


def home(request):
    students_list = Student.objects.all()
    context ={
        'object_list': students_list,
        'title':'Главная'
    }
    return render(request,'main/home.html',context)

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'You have new message from {name}({phone}): {message}')
    context = {
        'title': 'Контакты'
    }
    return render(request,'main/contact.html',context)


