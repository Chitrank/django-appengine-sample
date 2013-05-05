from django.conf.urls import patterns, include, url

urlpatterns = patterns('pastebin.views',
	(r'^$', 'new'),	
	(r'^(?P<id>\d+)', 'show'),
)
