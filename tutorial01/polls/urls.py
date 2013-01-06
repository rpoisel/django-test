from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns('views',
    url(r'^$', views.index, name='index'),
    # example: /polls/5/
    url(r'^(?P<poll_id>\d+)/$', detail, name='detail'),
    url(r'^(?P<poll_id>\d+)/results/$', results, name='results'),
    url(r'^(?P<poll_id>\d+)/vote/$', vote, name='vote'),
)
