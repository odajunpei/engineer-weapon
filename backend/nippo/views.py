from django.shortcuts import render, redirect
from .forms import FileFormset, NippoCreateForm


def nippo(request):
    form = NippoCreateForm(request.POST or None)
    context = {'form': form}
    if request.method == 'POST' and form.is_valid():
        post = form.save(commit=False)
        # 今回はファイルなのでrequest.FILESが必要
        formset = FileFormset(request.POST, files=request.FILES, instance=post)
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


def update_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = PostCreateForm(request.POST or None, instance=post)
    formset = FileFormset(request.POST or None,
                          files=request.FILES or None, instance=post)
    if request.method == 'POST' and form.is_valid() and formset.is_valid():
        form.save()
        formset.save()
        # 編集ページを再度表示
        return redirect('app:update_post', pk=pk)

    context = {
        'form': form,
        'formset': formset
    }

    return render(request, 'app/post_form.html', context)
