"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path("register/", RegisterView.as_view(), name="register"),
    path("", NoteListView.as_view(), name="note_list"),
    path("note/<int:pk>/", NoteDetailView.as_view(), name="note_detail"),
    path("note/add/", NoteCreateView.as_view(), name="note_add"),
    path("note/<int:pk>/edit/", NoteUpdateView.as_view(), name="note_edit"),
    path("note/<int:pk>/delete/", NoteDeleteView.as_view(), name="note_delete"),
    path("category/add/", CategoryCreateView.as_view(), name="category_add"),
    path("categories/", CategoryListView.as_view(), name="category_list"),
]