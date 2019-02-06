from django.shortcuts import render, redirect
from django.views.generic import View
# from django.http import HttpResponse

from .models import Post, Tag
from .utils import ObjectDetailMixin, ObjectListMixin
from .forms import TagForm


class PostsList(ObjectListMixin, View):
    model = Post
    template = 'blog/index.html'


class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'blog/post_detail.html'


class TagsList(ObjectListMixin, View):
    model = Tag
    template = 'blog/tags_list_url.html'


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'blog/tag_detail.html'


class TagCreate(View):
    def get(self, request):
        form = TagForm()
        return render(request, 'blog/tag_create.html', context={'form': form})

    def post(self, request):
        bound_form = TagForm(request.POST)

        if bound_form.is_valid():
            new_tag = bound_form.save()
            return redirect(new_tag)

        return render(request, 'blog/tag_create.html', context={'form': bound_form})
        



# Create your views here.
# def posts_list(request):
#     # Post.objects.all().delete()
#     # Post.objects.create(title='Заголовок-1', slug='slug_id_1', body='Тело поста-1')
    
#     posts = Post.objects.all()

#     return render(request, 'blog/index.html', context={'posts': posts})


# def get(self, request, slug):
#     # post = Post.objects.get(slug=slug)
#     post = get_object_or_404(Post, slug__iexact=slug)
#     return render(request, 'blog/post_detail.html', context={'post': post})


# def get(self, request, slug):
#     # tag = Tag.objects.get(slug__iexact=slug)
#     tag = get_object_or_404(Tag, slug__iexact=slug)
#     return render(request, 'blog/tag_detail.html', context={'tag': tag})


# def tags_list(request):
#     tags = Tag.objects.all()
#     return render(request, 'blog/tags_list_url.html', context={'tags': tags})