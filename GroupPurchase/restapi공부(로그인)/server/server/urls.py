from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
import user.serializer

app_name='user'

router = routers.DefaultRouter()
router.register('user',user.serializer.UserViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/', include((router.urls, 'user'), namespace='api')),
]