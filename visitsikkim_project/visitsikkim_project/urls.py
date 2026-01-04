
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

