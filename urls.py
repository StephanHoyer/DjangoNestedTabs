from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns('',
    url(r'^$', views.BaseView.as_view(), name='base'),
    url(r'^a/', views.AView.as_view(), name='a'),
    url(r'^b/', views.BView.as_view(), name='b'),
)
