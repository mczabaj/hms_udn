from django.conf.urls import url
from . import views

app_name = "participants"
urlpatterns = [
    url(r'^$', views.ParticipantList.as_view(), name='index'),
    url(r'^participants$', views.ParticipantList.as_view(), name='index'),
    url(r'^participants/new$', views.ParticipantCreate.as_view(), name='new'),
    url(r'^participants/(?P<pk>[0-9]+)/$', views.ParticipantUpdate.as_view(), name='detail'),
    url(r'^participants/create$', views.ParticipantCreate, name='create'),
    url(r'^participants/(?P<participant_id>[0-9]+)/update$', views.ParticipantUpdate, name='update'),
    url(r'^participants/(?P<participant_id>[0-9]+)/delete$', views.ParticipantDelete, name='delete'),
]
