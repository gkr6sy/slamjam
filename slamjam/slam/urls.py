from django.conf.urls import patterns, url
from slam import views

urlpatterns = patterns('',
	url(r'^$', views.home, name='home'),
    url(r'^about/$',views.about,name='about'),
    url(r'^search/$',views.search,name='search'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.exit, name='logout'),
)