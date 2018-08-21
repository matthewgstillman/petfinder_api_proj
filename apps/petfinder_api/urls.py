from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^barnyard_breeds$', views.barnyard_breeds, name="barnyard_breeds"),
    url(r'^bird_breeds$', views.bird_breeds, name="bird_breeds"),
    url(r'^cat_breeds$', views.cat_breeds, name="cat_breeds"),
    url(r'^dog_breeds$', views.dog_breeds, name="dog_breeds"),
    url(r'^find_dog$', views.find_dog, name="find_dog"),
    url(r'^find_pet$', views.find_pet, name="find_pet"),
    url(r'^reptile_breeds$', views.reptile_breeds, name="reptile_breeds"),
    url(r'^bird_search$', views.bird_search, name="bird_search"),
    url(r'^cat_search$', views.cat_search, name="cat_search"),
    url(r'^barnyard_search$', views.barnyard_search, name="barnyard_search"),
    url(r'^dog_search$', views.dog_search, name="dog_search"),
    url(r'^pet_search$', views.pet_search, name="pet_search"),
    url(r'^reptile_search$', views.reptile_search, name="reptile_search"),
]