from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),

<<<<<<< HEAD
    path("", include("accounts.urls")),
    path("", include("dashboard.urls")),
=======
    # Accounts App
    path("", include("accounts.urls")),
>>>>>>> c6a23d4c9b4edc97ebe68609e9631b62cbb01c7a

    # Fleet App
    path("fleet/", include("fleet.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)