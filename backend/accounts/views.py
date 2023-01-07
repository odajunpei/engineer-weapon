from django.views.generic import CreateView, UpdateView, DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth import get_user_model
from article.models import Article
from .models import User, Profile
from .forms import UserCreationForm


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'accounts/login_signup.html'
    success_url = '/'

    def form_valid(self, form):
        return super().form_valid(form)


class Login(LoginView):
    template_name = 'accounts/login_signup.html'

    def form_valid(self, form):
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


class AccountUpdateView(UpdateView):
    model = get_user_model()
    template_name = 'accounts/account.html'
    fields = ('username', 'email',)
    success_url = '/account/'

    def get_object(self):
        # URL変数ではなく、現在のユーザーから直接pkを取得
        self.kwargs['pk'] = self.request.user.pk
        return super().get_object()


class ProfileUpdateView(UpdateView):
    model = Profile
    template_name = 'accounts/profile.html'
    fields = ('name', 'zipcode', 'prefecture',
              'city', 'tel', 'image')
    success_url = '/'

    def get_object(self):
        # URL変数ではなく、現在のユーザーから直接pkを取得
        self.kwargs['pk'] = self.request.user.pk
        return super().get_object()


class ProfileDetailView(LoginRequiredMixin, DetailView):
    template_name = "accounts/profile_detail.html"
    model = Profile
