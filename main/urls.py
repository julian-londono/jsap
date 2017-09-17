from django.conf.urls import url
from django.contrib import admin
from main import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^login/$', auth_views.login, {'template_name': 'main/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^search/(?P<category>\w+)/(?P<value>\d+)/$', views.search, name='search'),
    url(r'^profile/(?P<name>\w+)/$', views.profile, name='profile'),
    url(r'^chatting/(?P<name>\w+)/$', views.chat, name='chat'),
]
