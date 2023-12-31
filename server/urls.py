from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from backend.views import UserView
from rest_framework import routers

router = routers.DefaultRouter()
router.register("", UserView, basename='userview')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
