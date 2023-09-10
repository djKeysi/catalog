from django.http import Http404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView,DetailView

from main.models import Category, Product


# def home(request): ProductListView
#     category_list = Category.objects.all()
#     context = {
#         'object_list': category_list
#     }
#     return render(request,'main/home.html',context)

class ProductListView(ListView):
    model = Product


# class CategoryListView(ListView):
#     model = Category

class ProductDetailView(DetailView):
    model = Product
    # template_name = 'main/student_form.html'
   # fields = ('name', 'price_for_buy')
    #success_url = reverse_lazy('main:index')

# def contacts(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         phone = request.POST.get('phone')
#         message = request.POST.get('message')
#         print(f'You have new message from {name}({phone}): {message}')
#     return render(request, 'main/contacts.html')

class ContactCreateView(CreateView):
    model = Product
    fields = ('name', 'phone','discription')#discription это message
    template_name = 'main/contacts.html'
    success_url = reverse_lazy('main:contacts')
# class PostView(DetailView):
#     model = Product
#     context_object_name = 'post'
#     template_name = 'private_post_detal.html'

    # def get_object(self):
    #     object = super(PostView, self).get_object()
    #     if not self.request.user.is_authenticated():
    #         raise Http404
    #     return object


# def categories(request):
#     category_list = Category.objects.all()
#     context = {
#         'object_list': category_list
#     }
#     return render(request,'main/categories.html',context)
#
#
#
# def category_products(request,pk):
#     #category_item = Category.objects.get(pk=pk)
#     category_list = Product.objects.filter(category_id=pk)
#     context = {
#         'object_list': category_list
#
#     }
#     return render(request,'main/products.html',context)
