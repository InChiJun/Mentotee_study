from django.contrib import admin
from django.urls import path
from django.views.generic.detail import DetailView

urlpatterns = [
    path('admin/', admin.site.urls),
]
