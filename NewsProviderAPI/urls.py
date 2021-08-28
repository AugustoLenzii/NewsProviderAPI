from django.contrib import admin
from django.urls import path, include
from news.urls import router

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls')),
]
