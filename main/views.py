from django.shortcuts import render

def home(request):
    return render(request,'main/home.html')

def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'You have new message from {name1}({phone}): {message}')
    return render(request,'main/contacts.html')
