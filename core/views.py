# from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView

from .models import Core


class IndexView(ListView):
    model = Core
    template_name = "core/index.html"
    context_object_name = "index"
    # context_object_name = "object_list" (default)


class SingleView(DetailView):
    model = Core
    template_name = "core/single.html"
    context_object_name = "post"


class PostsView(ListView):
    model = Core
    template_name = "core/posts.html"
    context_object_name = "post_list"


class AddView(CreateView):
    model = Core
    # fields = ["title"]
    fields = "__all__"
    template_name = "core/add.html"
    success_url = reverse_lazy("core:posts")
    # context_object_name = "object_list" (default)


class EditView(UpdateView):
    model = Core
    fields = "__all__"
    template_name = "core/edit.html"
    pk_url_kwarg = "pk"
    success_url = reverse_lazy("core:posts")
    # context_object_name = "object_list" (default)


class DeleteCustomView(DeleteView):
    model = Core
    # fields = "__all__"
    template_name = "core/confirm-delete.html"
    pk_url_kwarg = "pk"
    success_url = reverse_lazy("core:posts")
    # context_object_name = "object_list" (default)
