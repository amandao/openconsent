from django.conf.urls.defaults import patterns, url
from django.views.generic.list_detail import object_detail
from django.views.generic.simple import redirect_to

from publicweb.views import add_decision, add_decision_status, edit_decision, listing, \
                     export_csv
from publicweb.models import Decision

urlpatterns = patterns('openconsent.publicweb.views',
    url(r'^export_csv/$',
        export_csv,
        name='publicweb_export_csv'),
    url(r'^add/$',
        add_decision,
        name='publicweb_decision_add'),
    url(r'^add/(?P<status_id>[\d]+)/$',
        add_decision_status,
        name='publicweb_decision_add_status'),
    url(r'^edit/(?P<decision_id>[\d]+)/$', 
        edit_decision,
        name='publicweb_decision_edit'),
    url(r'^view/(?P<object_id>[\d]+)/$',
        object_detail,
        { 'queryset': Decision.objects.all(),
         'template_name': 'decision_detail.html'},
        name='publicweb_decision_view'),
    url(r'^list/(?P<status>[a-z]+)/$',
        listing,
        name='list'),
    url(r'^$', redirect_to, {'url': 'list/proposal/'}),
    )