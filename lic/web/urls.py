from django.conf.urls import include, url

from .views import HomeView, Login


urlpatterns = [
    url(r'^$', HomeView.as_view(), name="home"),
    url(r'^login/$', Login.as_view(), name="login")
]

