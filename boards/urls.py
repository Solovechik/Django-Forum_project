from django.urls import path, re_path

from . import views
from .views import PostUpdateView, BoardsListView, TopicListView, PostListView

urlpatterns = [
    path('', BoardsListView.as_view(), name='index'),
    re_path(r'^(?P<pk>\d+)/$', TopicListView.as_view(), name='board_topics'),
    re_path(r'^(?P<pk>\d+)/new/$', views.new_topic, name='new_topic'),
    re_path(r'^(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/$', PostListView.as_view(), name='topic_posts'),
    re_path(r'^(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/reply/$', views.reply_topic, name='reply_topic'),
    re_path(r'^(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/posts/(?P<post_pk>\d+)/edit/$', PostUpdateView.as_view(), name='edit_post')
]
