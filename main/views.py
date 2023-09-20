

from django.forms import inlineformset_factory
from django.http import Http404
from django.shortcuts import render
from django.urls import reverse_lazy,reverse
from django.views.generic import ListView, DetailView, CreateView, DetailView, UpdateView, DeleteView

from main.forms import ProductForm, VersionForm
from main.models import Category, Product, Version


# def home(request): ProductListView
#     category_list = Category.objects.all()
#     context = {
#         'object_list': category_list
#     }
#     return render(request,'main/home.html',context)

class ProductListView(ListView):
    model = Product
    context_object_name = 'products'

    # form_class = VersionForm
    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        products = Product.objects.all()
        for product in products:
            product.active_version = product.versions.filter(flag_of_the_current_version=True).first()
        context_data['products'] = products
        return context_data


# class VersionDetailView(DetailView):
#     model = Version


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('main:home')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm

    # success_url = reverse_lazy('main:home')

    def get_success_url(self):
        return reverse('main:product_update', args=[self.object.pk])

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormSet = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            formset = VersionFormSet(self.request.POST, instance=self.object)
        else:
            formset = VersionFormSet(instance=self.object)
        context_data['formset'] = formset
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('main:home')


# class CategoryListView(ListView):
#     model = Category

class ProductDetailView(DetailView):
    model = Product
    # template_name = 'main/student_form.html'


# fields = ('name', 'price_for_buy')
# success_url = reverse_lazy('main:index')

# def contacts(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         phone = request.POST.get('phone')
#         message = request.POST.get('message')
#         print(f'You have new message from {name}({phone}): {message}')
#     return render(request, 'main/contacts.html')

class ContactCreateView(CreateView):
    model = Product
    fields = ('name', 'phone', 'discription')  # discription это message
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
