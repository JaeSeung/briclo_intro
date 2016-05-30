from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^posts/new/$', views.post_new, name='post_new'),
    url(r'^posts/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^posts/(?P<post_pk>\d+)/comments/new/$', views.comment_new, name='comment_new'),

    # 무시
    url(r'^2/$', views.index2, name='index2'),
    url(r'^add/$', views.add, name='add'),
    url(r'^posts/$', views.post_list, name='post_list'),
    url(r'^download/$', views.download, name='download'),
]
