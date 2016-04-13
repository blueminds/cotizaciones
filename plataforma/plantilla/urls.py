from django.conf.urls import include, url
from plantilla import views
urlpatterns = [
    url(r'^$', views.index)
]
