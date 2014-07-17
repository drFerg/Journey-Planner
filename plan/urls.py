from django.conf.urls import patterns, url

from plan import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^paper/$', views.paper, name='paper'),
    url(r'^paper/post-card.html$', views.card, name='card'),
    url(r'^paper/post-list.html$', views.post_list, name='post_list')
)
