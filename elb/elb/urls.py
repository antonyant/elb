from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView

from django.views.generic import RedirectView

from django.contrib import admin
admin.autodiscover()

from views import galleries, galleries_tag

urlpatterns = patterns('',

    url(r'^$', TemplateView.as_view(template_name='base.html')),
    url(r'^photologue/', include('photologue.urls')),
    (r'^papers/', include('editorials.urls')), 
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    (r'^tinymce/', include('tinymce.urls')),
    (r'^$', RedirectView.as_view(url='/home/')),
    (r'^galleries/type/(?P<tag>[-\w]+)/$', galleries_tag),
    (r'^galleries/(?P<tag>[-\w]+)/(?P<slug>[-\w]+)/$', galleries),

)
urlpatterns += patterns('django.contrib.flatpages.views',
    (r'^(?P<url>.*/)$', 'flatpage'),
)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
                            url(r'^__debug__/', include(debug_toolbar.urls)),
                            )
