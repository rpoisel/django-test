import os

from django.template import Context, loader
from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response, get_object_or_404

from polls.models import Poll


def index(request):
    # latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
    latest_poll_list = Poll.objects.order_by('-pub_date')
    # example: hard-coded
    # output = ', '.join([p.question for p in latest_poll_list])
    # example: explicitly rendered view
    # t = loader.get_template(os.path.join('polls', 'index.html'))
    # c = Context({
    #    'latest_poll_list': latest_poll_list,
    #    })
    # return HttpResponse(t.render(c))
    # example: implicitly rendered view
    return render_to_response(
            os.path.join('polls', 'index.html'),
            {'latest_poll_list': latest_poll_list}
            )


def detail(request, poll_id):
    # example: explicitly query for requested object
    # try:
    #    p = Poll.objects.get(pk=poll_id)
    # except Poll.DoesNotExist:
    #    raise Http404
    p = get_object_or_404(Poll, pk=poll_id)
    return render_to_response(os.path.join(
        'polls', 'detail.html'),
        {'poll': p}
        )


def results(request, poll_id):
    return HttpResponse("You are looking at the results of poll %s. "
            % poll_id)


def vote(request, poll_id):
    return HttpResponse("You are voting on poll %s. " % poll_id)


def error(request):
    return HttpResponse("This is the error-page that you requested. ")
