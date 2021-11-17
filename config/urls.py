from django.contrib import admin
from django.urls import path, include
from bookapi.views import BooksViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'books',BooksViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
]
