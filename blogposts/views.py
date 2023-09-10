from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from pytils.translit import slugify

from blogposts.models import BlogPost


class BlogPostListView(ListView):
    model = BlogPost

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogPostCreateView(CreateView):
    model = BlogPost
    fields = ('title', 'body',)
    success_url = reverse_lazy('blogpost:list')

    def form_valid(self, form):  # pip install pytils
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()

        return super().form_valid(form)


class BlogPostDetailView(DetailView):
    model = BlogPost

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class BlogPostDeleteView(DeleteView):
    model = BlogPost
    fields = ('title', 'body',)
    success_url = reverse_lazy('blogpost:list')


class BlogPostUpdateView(UpdateView):
    model = BlogPost
    fields = ('title', 'body','picture')

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blogpost:view', args=[self.kwargs.get('pk')])
