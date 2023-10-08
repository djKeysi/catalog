from django.forms import inlineformset_factory
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from main.forms import ProductForm, VersionForm
from main.models import Product, Version


class ProductListView(ListView):
    model = Product
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        products = Product.objects.all()
        for product in products:
            product.active_version = product.versions.filter(flag_of_the_current_version=True).first()
        context_data['products'] = products
        return context_data


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('main:home')

    def form_valid(self, form):
        self.object = form.save()
        self.object.user = self.request.user
        self.object.save()



        return super().form_valid(form)


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm

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


class ProductDetailView(DetailView):
    model = Product


class ContactCreateView(CreateView):
    model = Product
    fields = ('name', 'phone', 'discription')  # discription это message
    template_name = 'main/contacts.html'
    success_url = reverse_lazy('main:contacts')
