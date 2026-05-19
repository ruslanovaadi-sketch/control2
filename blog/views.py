from django.shortcuts import render
from django.views.generic import (
    ListView, DetailView,
    CreateView, UpdateView, DeleteView, View
)
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm

from .models import Note, Category


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("login")

class NoteListView(ListView):
    model = Note
    template_name = "notes/note_list.html"
    context_object_name = "notes"
    paginate_by = 10

    def get_queryset(self):
        qs = Note.objects.filter(user=self.request.user)

        # фильтр по категории
        category = self.request.GET.get("category")
        if category:
            qs = qs.filter(category_id=category)

        # поиск по заголовку
        search = self.request.GET.get("search")
        if search:
            qs = qs.filter(title__icontains=search)

        # закрепленные сверху
        return qs.order_by("-is_pinned", "-created_at")
    
class NoteDetailView(DetailView):
    model = Note
    template_name = "notes/note_detail.html"

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)

class NoteCreateView(CreateView):
    model = Note
    fields = ["title", "content", "category", "is_pinned"]
    template_name = "notes/note_form.html"
    success_url = reverse_lazy("note_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class NoteUpdateView(UpdateView):
    model = Note
    fields = ["title", "content", "category", "is_pinned"]
    template_name = "notes/note_form.html"
    success_url = reverse_lazy("note_list")

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)

class NoteDeleteView(DeleteView):
    model = Note
    template_name = "notes/note_confirm_delete.html"
    success_url = reverse_lazy("note_list")

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)

class CategoryCreateView(CreateView):
    model = Category
    fields = ["name"]
    template_name = "categories/category_form.html"
    success_url = reverse_lazy("note_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class CategoryListView(ListView):
    model = Category
    template_name = "categories/category_list.html"

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)

class TogglePinView(View):
    def post(self, request, pk):
        note = Note.objects.get(pk=pk, user=request.user)
        note.is_pinned = not note.is_pinned
        note.save()
        return redirect("note_list")                            
