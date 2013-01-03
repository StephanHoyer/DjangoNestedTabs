from django.conf.urls import patterns, include, url
from views import BaseView, AView, AAView, ABView, BView, BAView, BBView

urlpatterns = patterns('',
    url(r'^$', BaseView.as_view(), name='base'),
    url(r'^a/$', AView.as_view(), name=AView.url_name),
    url(r'^a/a/$', AAView.as_view(), name=AAView.url_name),
    url(r'^a/b/$', ABView.as_view(), name=ABView.url_name),
    url(r'^b/$', BView.as_view(), name=BView.url_name),
    url(r'^b/a/$', BAView.as_view(), name=BAView.url_name),
    url(r'^b/b/$', BBView.as_view(), name=BBView.url_name),
)
