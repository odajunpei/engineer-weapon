from django.shortcuts import render, redirect
from .forms import FileFormset, NippoCreateForm
import os
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Nippo, NippoDetail, Time
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
User = get_user_model


def nippo(request):
    form = NippoCreateForm(request.POST or None)
    context = {'form': form}
    if request.method == 'POST' and form.is_valid():
        post = form.save(commit=False)
        post.user = request.user
        formset = FileFormset(request.POST, instance=post)
        if formset.is_valid():
            post.save()
            formset.save()
            return redirect('nippo:nippo_list')

        # エラーメッセージつきのformsetをテンプレートへ渡すため、contextに格納
        else:
            context['formset'] = formset

    # GETのとき
    else:
        # 空のformsetをテンプレートへ渡す
        context['formset'] = FileFormset()

    return render(request, 'nippo/nippo_form.html', context)


def update(request, pk):
    nippo = get_object_or_404(Nippo, pk=pk)
    form = NippoCreateForm(request.POST or None,
                           instance=request.user and nippo)
    formset = FileFormset(request.POST or None,
                          instance=nippo)
    if request.method == 'POST' and form.is_valid() and formset.is_valid():
        form.save()
        formset.save()
        return redirect('nippo:nippo_detail', pk=pk)

    context = {
        'form': form,
        'formset': formset
    }

    return render(request, 'nippo/nippo_form.html', context)

# class NippoUpdateView(LoginRequiredMixin, UpdateView):
#     template_name = 'nippo/nippo_form.html'
#     model = Nippo
#     form_class = NippoCreateForm
#     formset_class = FileFormset

#     def get_success_url(self):
#         return reverse_lazy("nippo:nippo_detail", kwargs={'pk': self.object.pk})


class NippoListView(LoginRequiredMixin, ListView):
    template_name = 'nippo/nippo_list.html'
    model = Nippo


class NippoMyListView(LoginRequiredMixin, ListView):
    template_name = 'nippo/nippo_mylist.html'
    model = Nippo


class NippoDetailView(LoginRequiredMixin, DetailView):
    template_name = 'nippo/nippo_detail.html'
    model = Nippo


class NippoDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'nippo/nippo_delete.html'
    model = Nippo
    success_url = reverse_lazy("nippo:nippo_list")
