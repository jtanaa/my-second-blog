from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # Your other URL patterns go here
    path('admin/', admin.site.urls),
]
