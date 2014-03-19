from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'editorials.views.editorial_list', name="editorial_list"),
    url(r'^archive/$', 'editorials.views.editorial_archive', name="editorial_archive"),
    url(r'^(?P<pk>[-\d]+)/', 'editorials.views.editorial_detail', name="editorial_detail"),
    
    
)
