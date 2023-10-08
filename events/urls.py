from django.urls import re_path
from . import views

app_name = 'events'

urlpatterns = [
    re_path(r'^e/$', views.event_list, name="list"),

    re_path(r'^create/$', views.event_create, name="create"),
    re_path(r'(?P<slug_register>[\w-]+)/register$', views.event_register, name="register"),
#          (?P<slug_register>[\w-]+)/register$

    re_path(r'(?P<slug>[\w-]+)/$', views.event_detail, name="detail"),

]
