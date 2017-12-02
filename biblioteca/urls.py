from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.livros_list, name='livros_list'),
]
