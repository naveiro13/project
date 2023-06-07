from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from home import views

app_name = "home"

urlpatterns = [
    path("", views.index, name="index"),
]

urlpatterns += staticfiles_urlpatterns()
