from django.contrib import messages
from django.http import JsonResponse, HttpResponse
from django.views.generic import CreateView
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from blog.models import Post
from blog.forms import PostForm, CommentForm


def index(request):
    post_list = Post.objects.all()[:10]
    return render(request, 'blog/index.html', {
        'post_list': post_list,
    })


def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            # form.cleaned_data
            post = form.save()
            # return redirect('blog:post_detail', post.pk)
            return redirect(post)
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {
        'form': form,
    })

post_new = CreateView.as_view(model=Post, form_class=PostForm)


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'blog/post_detail.html', {
        'post': post,
    })


def comment_new(request, post_pk):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)  # 내부 모델 인스턴스의 save() 함수를 호출하지 말고, 그냥 리턴하라.
            comment.post = Post.objects.get(pk=post_pk)
            comment.save()
            messages.error(request, '새 댓글을 저장했습니다.')
            return redirect('blog:post_detail', comment.post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/comment_form.html', {
        'form': form,
    })


def index2(request):
    context = {}
    html = render_to_string('blog/index.html', context)
    return HttpResponse(html)


def add(request):
    result = int(request.GET['x']) + int(request.GET['y'])
    return HttpResponse(str(result))


def post_list(request):
    format = request.GET.get('format', 'html')

    posts = ['제목1', '제목2', '제목3']
    if format == 'json':
        return JsonResponse(posts, safe=False)
    return render(request, 'blog/post_list.html', {
        'posts': posts,
    })


def download(request):
    csv_content = '''col1,col2,col3
col4,col5,col6'''
    response = HttpResponse(csv_content, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="report.csv"'
    return response

