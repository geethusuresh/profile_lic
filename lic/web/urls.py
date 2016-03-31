from django.conf.urls import include, url

from .views import HomeView, Login, Logout


urlpatterns = [
    url(r'^$', HomeView.as_view(), name="home"),
    url(r'^login/$', Login.as_view(), name="login"),
    url(r'^logout/$', Logout.as_view(), name="logout"),
]

