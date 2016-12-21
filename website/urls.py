from django.conf.urls import url

from website import views



urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^tour/$', views.tour, name='tour'),

]