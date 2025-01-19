from django.http import HttpResponseNotAllowed
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

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


class PostsView(LoginRequiredMixin, ListView):
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



def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()  # Pobierz użytkownika
            login(request, user)    # Zaloguj użytkownika
            return redirect("/")  # Przekierowanie na stronę główną lub inną po zalogowaniu
    else:
        form = AuthenticationForm()

    return render(request, "core/login.html", {'form': form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, "You were succesfully logged out.")  # Dodaj wiadomość
        return redirect('/')  # Przekierowanie po wylogowaniu

    return HttpResponseNotAllowed(['POST'])  # Obsługuje tylko POST
