from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('tasks.api_urls')),
    path('accounts/', include('accounts.urls')),
    path('', include('tasks.urls')),
]