from django.shortcuts import render

from main.models import Category


def home(request):
    category_list = Category.objects.all()
    context = {
        'object_list': category_list
    }
    return render(request,'main/home.html',context)

def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'You have new message from {name}({phone}): {message}')
    return render(request,'main/contacts.html')
