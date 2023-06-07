from django.urls import path

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import index
from home import views

# Es necesario este nombre, para ser llamado desde la plantila,
# por ejemplo: {% url 'cliente:index' %}

app_name = "venta"

urlpatterns = [
    path("", index, name="index"),
]
urlpatterns += staticfiles_urlpatterns()
