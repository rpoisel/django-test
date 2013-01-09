import os

from django.conf.urls import patterns, url
from django.views.generic import DetailView, ListView

from polls.models import Poll

urlpatterns = patterns('polls.views',
    url(r'^$', ListView.as_view(
            queryset=Poll.objects.order_by('-pub_date'),
            context_object_name='latest_poll_list',
            template_name=os.path.join('polls', 'index.html'))),
    # example: /polls/5/
    url(r'^(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Poll,
            template_name=os.path.join('polls', 'detail.html'))),
    url(r'^(?P<pk>\d+)/results/$',
        DetailView.as_view(
            model=Poll,
            template_name=os.path.join('polls', 'results.html')),
        name='poll_results'),
    url(r'^(?P<poll_id>\d+)/vote/$', 'vote'),
)
