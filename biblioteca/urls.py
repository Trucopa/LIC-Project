from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.emprestimos_list, name='emprestimos_list'),
    url(r'^emprestimo/(?P<pk>[0-9]+)/$', views.emprestimo_detail, name='emprestimo_detail'),
]
