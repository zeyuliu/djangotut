from django.http import HttpResponse
from polls.models import Poll
from django.template import Context, loader
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.shortcuts import render_to_response
from django.template import RequestContext

def index(request):
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    return render_to_response('polls/index.html', context_instance=RequestContext(request))

def detail(request, poll_id):
	return HttpResponse("You're looking at poll %s." % poll_id)

def results(request, poll_id):
	return HttpResponse("You're looking at the results of poll %s." %poll_id)

def vote(request, poll_id):
	return HttpResponse("You're voting on poll %s." % poll_id)

