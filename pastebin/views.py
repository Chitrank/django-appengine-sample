from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.urlresolvers import reverse

from pastebin.models import Paste

def show(request, id):
	pasted = get_object_or_404(Paste, pk=int(id))
	return render_to_response('paste.html',
					{'pasted': pasted.text},
					context_instance=RequestContext(request))

def new(request):
	if request.POST.has_key('text'):
		pasted = Paste()
		pasted.text = request.POST['text']
		pasted.save()
		return HttpResponseRedirect(reverse('pastebin.views.show', kwargs={'id': pasted.id}))
#		return HttpResponseRedirect("/%i/" % pasted.id)
	else:
		return render_to_response('input.html',
			context_instance=RequestContext(request))
