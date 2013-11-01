from django.shortcuts import render_to_response
from django.template import RequestContext
from news.models import News

def NewsAll(request):
	news = News.objects.all().order_by('title')
	context = {'news': news}
	return render_to_response('newsall.html', context, context_instance=RequestContext(request))