from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.emprestimos_list, name='emprestimos_list'),
    url(r'^livros/$', views.livros_list, name='livros_list'),
    url(r'^livros/new/$', views.livro_new, name='livro_new'),
    url(r'^emprestimo/(?P<pk>[0-9]+)/$', views.emprestimo_detail, name='emprestimo_detail'),
    url(r'^emprestimo/new/$', views.emprestimo_new, name='emprestimo_new'),

]
