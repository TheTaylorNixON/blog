from django.shortcuts import render, redirect
from django.views.generic import View
# from django.http import HttpResponse

from .models import Post, Tag
from .utils import *
from .forms import TagForm, PostForm

from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

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


class TagCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    model = TagForm
    template = 'blog/tag_create.html'
    raise_exception = True


class PostCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    model = PostForm
    template = 'blog/post_create.html'
    raise_exception = True


class TagUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Tag
    form = TagForm
    template = 'blog/tag_update_form.html'
    raise_exception = True


class PostUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Post
    form = PostForm
    template = 'blog/post_update_form.html'
    raise_exception = True


class TagDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Tag
    template = 'blog/tag_delete_form.html'
    url = 'tags_list_url'
    raise_exception = True


class PostDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Post
    template = 'blog/post_delete_form.html'
    url = 'posts_list_url'
    raise_exception = True












# class TagUpdate(View):
#     def get(self, request, slug):
#         tag = Tag.objects.get(slug__iexact=slug)
#         bound_form = TagForm(instance=tag)
#         return render(request, 'blog/tag_update_form.html', context={'form': bound_form, 'tag': tag})

#     def post(self, request, slug):
#         tag = Tag.objects.get(slug__iexact=slug)
#         bound_form = TagForm(request.POST, instance=tag)

#         if bound_form.is_valid():
#             new_tag = bound_form.save()
#             return redirect(new_tag)

#         return render(request, 'blog/tag_update_form.html', context={'form': bound_form, 'tag': tag})






# class TagCreate(View):
#     def get(self, request):
#         form = TagForm()
#         return render(request, 'blog/tag_create.html', context={'form': form})

#     def post(self, request):
#         bound_form = TagForm(request.POST)

#         if bound_form.is_valid():
#             new_tag = bound_form.save()
#             return redirect(new_tag)

#         return render(request, 'blog/tag_create.html', context={'form': bound_form})
        

# class PostCreate(View):
#     def get(self, request):
#         form = PostForm()
#         return render(request, 'blog/post_create.html', context={'form': form})

#     def post(self, request):
#         bound_form = PostForm(request.POST)

#         if bound_form.is_valid():
#             new_post = bound_form.save()

#             return redirect(new_post)

#         return render(request, 'blog/post_create.html', context={'form': bound_form})





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