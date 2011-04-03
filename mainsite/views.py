from datetime import datetime

from django.conf import settings
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.views.generic.list_detail import object_list

from csesoc import settings
from csesoc.mainsite.models import Static
from csesoc.sponsors.views import sponsorsList

# presently using generic views for everything. add custom views here as needed

def streamitem_index(request, queryset, **kwargs):
    context = {
        'request': request,
        'queryset': queryset.filter(pub_date__lte=datetime.now()).order_by('-pub_date'),
        'paginate_by': settings.STREAMITEMS_PER_PAGE,
        'template_name': 'mainsite/streamitem_archive.html',
        'extra_context': {'allSponsors' : sponsorsList(request)},
    }
    return object_list(**context)

def static(request, path):
    p = get_object_or_404(Static, slug=path.replace('/','_'))
    return render_to_response('static.html', { 'allSponsors' : sponsorsList(request), 'object' : p }, context_instance=RequestContext(request) )

def thedate(request):
    return render_to_response('thedate.html', { 'date' : datetime.now() }, context_instance=RequestContext(request) )

def calendar(request):
    return render_to_response('calendar.html', { 'nav' : "home", 'subnav' : "calendar" }, context_instance=RequestContext(request) )
