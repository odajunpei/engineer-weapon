# from django.shortcuts import render, redirect
# from .forms import NippoDetailCreateFormSet


# def nippo(request):
#     formset = NippoDetailCreateFormSet(request.POST or None)
#     if request.method == 'POST' and formset.is_valid():
#         formset.user = request.user
#         formset.save()
#         return redirect('article:article_list')

#     context = {
#         'formset': formset
#     }

#     return render(request, 'nippo/nippo_form.html', context)
