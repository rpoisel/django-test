from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns('polls.views',
    url(r'^$', 'index'),
    # example: /polls/5/
    url(r'^(?P<poll_id>\d+)/$', 'detail'),
    url(r'^(?P<poll_id>\d+)/results/$', 'results'),
    url(r'^(?P<poll_id>\d+)/vote/$', 'vote'),
)
