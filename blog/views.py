from django.shortcuts import render
from django.http import HttpResponse

from .models import Post, Tag

# Create your views here.


def posts_list(request):
    # Post.objects.all().delete()
    # Post.objects.create(title='Заголовок-1', slug='slug_id_1', body='Тело поста-1')
    # Post.objects.create(title='Заголовок-2', slug='slug_id_2', body='Тело поста-2')
    # Post.objects.create(title='Заголовок-3', slug='slug_id_3', body='Тело поста-3')
    # Post.objects.create(title='Заголовок-4', slug='slug_id_4', body='Тело поста-4')
    # Post.objects.create(title='Заголовок-5', slug='slug_id_5', body='Тело поста-5')
    posts = Post.objects.all()

    return render(request, 'blog/index.html', context={'posts': posts} )


def post_detail(request, slug):
    post = Post.objects.get(slug=slug)

    return render(request, 'blog/post_detail.html', context={'post': post})


def tags_list(request):
    tags = Tag.objects.all()

    return render(request, 'blog/tags_list_url.html', context={'tags': tags})


def tag_detail(request, slug):
    tag = Tag.objects.get(slug__iexact=slug)

    return render(request, 'blog/tag_detail.html', context={'tag': tag})