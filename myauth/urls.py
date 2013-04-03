from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myauth.views.home', name='home'),
    # url(r'^myauth/', include('myauth.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    #login page
    #url(r'^login/', 'django.views.login'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    #(r'', include('django.contrib.auth.urls')),
)
