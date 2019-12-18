from django.shortcuts import render , get_object_or_404
from .models import Post , Comment
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import CommentForm
# Создадим функцию отображения наших постов
def post_list(request):
    posts = Post.published.all()
    return render(request, 'blog/post/list.html', {'posts': posts})


# def post_detail(request, year, month, day, post):
#     post = get_object_or_404(Post, slug=post, status='published',publish__year=year,
#     publish__month=month,publish__day=day)
    # return render(request,'blog/post/detail.html',{'post': post})
def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,status='published',publish__year=year,
    publish__month=month,publish__day=day)
    # Список активных комментариев для этой статьи.
    comments = post.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        # Пользователь отправил комментарий.
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Создаем комментарий, но пока не сохраняем в базе данных.
            new_comment = comment_form.save(commit=False)
            # Привязываем комментарий к текущей статье.
            new_comment.post = post
            # Сохраняем комментарий в базе данных.
            new_comment.save()
        else:
            comment_form = CommentForm()
    comment_form = CommentForm()
    new_comment = None
    return render(request,'blog/post/detail.html',{'post': post,
    'comments': comments,
    'new_comment': new_comment,
    'comment_form': comment_form})

# def post_share(request, post_id):
#     # Получение статьи по идентификатору.
#     post = get_object_or_404(Post, id=post_id,status='published')
#     if request.method == 'POST':
#         # Форма была отправлена на сохранение.
#         form = EmailPostForm(request.POST)
#         if form.is_valid():
#         # Все поля формы прошли валидацию.
#             cd = form.cleaned_data
#             # ... Отправка электронной почты.
#     else:
#         form = EmailPostForm()
#         return render(request, 'blog/post/share.html',
#         {'post': post, 'form': form})

# def post_list(request):
#     object_list = Post.published.all()
#     paginator = Paginator(object_list, 1) # По 3 статьи на каждой странице.
#     page = request.GET.get('page')
#     try:
#         posts = paginator.page(page)
#     except PageNotAnInteger:
#         # Если страница не является целым числом, возвращаем первую страницу.
#         posts = paginator.page(1)
#     except EmptyPage:
#         # Если номер страницы больше, чем общее количество страниц, возвращаем последнюю.
#         posts = paginator.page(paginator.num_pages)
#     return render(request,'blog/post/list.html', {'page': page, 'posts': posts})
