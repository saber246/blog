
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import RegisterForm
from .models import Post

# Create your views here
 
def index(request):
    posts = Post.objects.all().order_by('-created_at')
    context = {
        'posts': posts,
        'title': 'MyBlog首页'
    }
    return render(request, 'index.html', context)

def index_detail(request, pk):
    post = Post.objects.get(pk=pk)
    conetxt = {
        'post': post,
        'title': f'{post.title} - 详情'
    }
    return render(request, 'index_detail.html', conetxt)

def register(request):
    if request.user.is_authenticated:
        messages.success(request, '注册成功，欢迎你')
        return redirect('index')
    elif request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'注册成功，欢迎你，{user.username}！')
            return redirect('index')
        else:
            messages.error(request, '注册失败！请检查输入信息！')
            return HttpResponse('注册失败！请检查输入信息！')
    else:
        form = RegisterForm()
        return render(request, 'register.html', {
            'form': form,
            'title': '注册'
        })
        
@login_required # type: ignore
def toggle_favorite(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.favorites.filter(id=request.user.id).exists():
        post.favorites.remove(request.user)
    else:
        post.favorites.add(request.user)
    referer = request.META.get('HTTP_REFERER', '/oooooooo')
    return redirect(referer)

@login_required
def favorites(request):
    posts = request.user.favorite_posts.all()
    return render(request, 'favorites.html', {
        'posts': posts,
        'title': '收藏夹'
    })
        
    