from django.urls import path,include
from rest_framework import routers
from .views import NewsViewSets

router = routers.SimpleRouter()
router.register('news', NewsViewSets, basename='news')

urlpatterns = [
    path('', include(router.urls)),
]