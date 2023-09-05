from django.shortcuts import render

from main.models import Category, Product


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


def categories(request):
    category_list = Category.objects.all()
    context = {
        'object_list': category_list
    }
    return render(request,'main/categories.html',context)



def category_products(request,pk):
    #category_item = Category.objects.get(pk=pk)
    category_list = Product.objects.filter(category_id=pk)
    context = {
        'object_list': category_list

    }
    return render(request,'main/products.html',context)