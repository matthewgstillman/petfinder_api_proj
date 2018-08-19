from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^cat_breeds$', views.cat_breeds, name="cat_breeds"),
]