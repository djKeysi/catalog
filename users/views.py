import random
import secrets

from django.conf import settings

from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.core.mail import send_mail
from django.shortcuts import HttpResponseRedirect

from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, TemplateView

from users.forms import UserRegisterForm, UserForm
#from users.forms import UserRegisterForm,UserForm
from users.models import User,EmailVerification


# Create your views here.
class LoginView(BaseLoginView):
    template_name = 'users/login.html'

class VerifyView(TemplateView):
    template_name = 'users/verify.html'


class LogoutView(BaseLogoutView):
    pass

class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:verify')
    template_name = 'users/register.html'

    #redirect(reverse('users:verify'))

    #redirect('users/verify.html')


    # def form_valid(self, form):
    #     if form.is_valid():
    #         self.object = form.save(commit=False)
    #
    #         #self.object = form.save()
    #
    #         send_mail(
    #             subject='Добро пожаловать',
    #             message='на платформу',
    #             from_email=settings.EMAIL_HOST_USER,
    #             recipient_list=[self.object.email]
    #         )
    #     return super().form_valid(form)


    # def form_valid(self, form):
    #     if form.is_valid():
    #         self.object = form.save(commit=False)
    #         code = secrets.token_urlsafe(nbytes=8)
    #         self.object.is_verified_email = code
    #         self.object.save()
    #
    #         url = reverse('users:verify',args=[code])
    #         #servises.send_verify(url,self.object.email)
    #         send_mail(url,self.object.email)
    #
    #     return super().form_valid(form)
    #
    # def verify():





class UserUpdateView(UpdateView):
    model = User
    success_url = reverse_lazy('users:profile')
    form_class = UserForm

    def get_object(self, queryset=None):
        return self.request.user

def generate_new_password(request):
    new_password = ''.join([str(random.randint(0,9)) for _ in range(12)])
    send_mail(
        subject='Вы сменили пароль',
        message=f'Ваш новый пароль: {new_password} ',
        from_email=settings.EMAIL_HOST_USER,
        # recipient_list = [new_user.email, new_user.password]
        recipient_list=[request.user.email]

    )
    request.user.set_password('')
    request.user.save()
    return redirect(reverse('main:home'))


class EmailVerificationView(TemplateView):
    template_name = 'users/email_verification.html'

    def get(self, request, *args, **kwargs):
        code = kwargs['code']
        user = User.objects.get(email=kwargs['email'])
        email_verifications = EmailVerification.objects.filter(user=user, code=code)
        if email_verifications.exists() and not email_verifications.first().is_expired():
            user.is_verified_email = True
            user.save()
            return super(EmailVerificationView, self).get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('/'))
