from accounts.models import User, Profile
import os
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from .forms import CaseForm, DetailForm
from .models import Case, Detail, Shop, Status
from django.http import JsonResponse
from django.views import generic
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse, reverse_lazy
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
User = get_user_model


class CaseListView(LoginRequiredMixin, ListView):
    template_name = "case/case_list.html"
    model = Case


class CaseMyListView(LoginRequiredMixin, ListView):
    template_name = "case/case_mylist.html"
    model = Case


class CaseDetailView(LoginRequiredMixin, DetailView):
    template_name = "case/case_detail.html"
    model = Case


class CaseCreateView(LoginRequiredMixin, CreateView):
    template_name = "case/case_form.html"
    model = Case
    form_class = CaseForm

    def get_success_url(self):
        return reverse_lazy("case:case_detail", kwargs={'pk': self.object.pk})


class CaseUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "case/case_form.html"
    model = Case
    form_class = CaseForm

    def get_success_url(self):
        return reverse_lazy("case:case_detail", kwargs={'pk': self.object.pk})


class CaseDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "case/case_delete_form.html"
    model = Case


class DetailCreateView(LoginRequiredMixin, CreateView):
    template_name = "detail/detail_form.html"
    model = Detail
    form_class = DetailForm

    def form_valid(self, form):
        case_pk = self.kwargs.get('pk')
        case = get_object_or_404(Case, pk=case_pk)
        detail = form.save(commit=False)
        detail.user = self.request.user
        detail.case = case
        detail.save()
        return redirect('case:case_detail', pk=case_pk)


class DetailDetailView(LoginRequiredMixin, DetailView):
    template_name = "detail/detail_detail.html"
    model = Detail


class DetailUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "detail/detail_form.html"
    model = Detail
    form_class = DetailForm

    def get_success_url(self):
        return reverse_lazy("case:detail_detail", kwargs={'pk': self.object.pk})


class DetailDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "detail/detail_delete.html"
    model = Detail

    def get_success_url(self):
        return reverse_lazy("case:case_detail", kwargs={'pk': self.object.pk})


class ShopDetailView(LoginRequiredMixin, DetailView):
    template_name = "shop/shop_detail.html"
    model = Shop

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shop_list'] = Shop.objects.all()
        context['case_list'] = self.object.case_shop.all()
        return context
