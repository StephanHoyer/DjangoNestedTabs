from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns('',
    url(r'^$', views.BaseView.as_view(), name='base'),
    url(r'^a/$', views.AView.as_view(), name='a'),
    url(r'^a/a/$', views.AAView.as_view(), name='aa'),
    url(r'^a/b/$', views.ABView.as_view(), name='ab'),
    url(r'^b/$', views.BView.as_view(), name='b'),
    url(r'^b/a/$', views.BAView.as_view(), name='ba'),
    url(r'^b/b/$', views.BBView.as_view(), name='bb'),
)
