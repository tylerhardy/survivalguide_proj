"""Defines URL patterns for main_app."""
from django.conf.urls import url
from .views import HomePageView, SignUpView

urlpatterns = [
    url(r'^$', HomePageView.as_view(), name="home"),
    url(r'^accounts/register/$', SignUpView.as_view(), name='signup'),
]