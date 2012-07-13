from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import Context, loader
from django.template import RequestContext

from c2g.db_test_data import *

### C2G Core Views ###

def home(request):
	return render_to_response('base.html', {'request': request}, context_instance=RequestContext(request))

def healthcheck(request):
    return HttpResponse("I'm alive!")

