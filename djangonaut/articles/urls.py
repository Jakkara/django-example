from django.conf.urls import url
from . import views

app_name = 'articles' ##namespaces this file

urlpatterns = [
    url(r'^$', views.article_list, name='list'),
    url(r'^(?P<slug>[\w-]+)/$', views.article_detail, name='detail') #handles url slugs and hands them off to views
]
