from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.homepage, name="home"),
    url(r'^discuss/(.*)/$', views.discussion, name="discussion"),
    url(r'^start-discussion/$', views.StartDiscussionView.as_view(), name="start-discussion"),
    url(r'^profile/me/$', views.myprofile, name="myprofile"),
    url(r'^profile/(.*)/$', views.profile, name="profile"),
    url(r'^create-profile/$', views.CreateProfileView.as_view(), name="create_profile"),

    url(r'^api/posts/(?P<post_id>\d+)/upvote$', views.upvote_post, name="upvote_post"),
    url(r'^api/posts/(?P<post_id>\d+)/downvote$', views.downvote_post, name="downvote_post"),
    url(r'^api/posts/(?P<post_id>\d+)/undovote$', views.undo_vote_on_post, name="undo_vote_on_post"),
    
]