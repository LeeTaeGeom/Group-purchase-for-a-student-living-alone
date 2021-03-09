from django.conf.urls import include
from django.urls import path
from django.contrib import admin
from rest_framework import routers
from .views import FundingViewSet,FundingParticipantsViewSet


router = routers.DefaultRouter
router.register('funding',FundingViewSet)
router.register('funding/participants',FundingParticipantsViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    ]