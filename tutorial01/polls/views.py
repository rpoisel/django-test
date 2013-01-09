import os

from django.template import Context, loader, RequestContext
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
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
        {'poll': p},
        context_instance=RequestContext(request)
        )


def results(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    return render_to_response(
            os.path.join('polls', 'results.html'),
            {'poll': p}
            )


def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form.
        return render_to_response('polls/detail.html', {
            'poll': p,
            'error_message': "You didn't select a choice.",
        }, context_instance=RequestContext(request))
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(
                reverse(
                    'polls.views.results',
                    args=(p.id,)
                    )
                )


def error(request):
    return HttpResponse("This is the error-page that you requested. ")
