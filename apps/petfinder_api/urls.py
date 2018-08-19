from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^bird_breeds$', views.bird_breeds, name="bird_breeds"),
    url(r'^cat_breeds$', views.cat_breeds, name="cat_breeds"),
    url(r'^dog_breeds$', views.dog_breeds, name="dog_breeds"),
    url(r'^reptile_breeds$', views.reptile_breeds, name="reptile_breeds"),
]