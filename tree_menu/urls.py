from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.dynamic_view, name='home'),
    re_path(r'^(?P<path>.*)/$', views.dynamic_view, name='dynamic_view'),
]
