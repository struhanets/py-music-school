from django.urls import path, include
from rest_framework import routers

from musician.views import MusicianViewSet

app_name = "musician"

router = routers.SimpleRouter()
router.register("manage", MusicianViewSet, basename="manage")
urlpatterns = [
    path("", include(router.urls)),
]
