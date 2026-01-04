"""
URL configuration for visitsikkim_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include   # ✅ include is needed here
from django.conf import settings        # ✅ settings for serving media
from django.conf.urls.static import static  # ✅ static() helper

urlpatterns = [
    path('admin/', admin.site.urls),   # ✅ admin URL works now
    path('', include("main.urls")), 
    # path("", include("chatapp.urls")),
    
          # ✅ includes your app's urls
]

# Serve media files (images) during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
