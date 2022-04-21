from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('useraccounts.urls')),
    path('api/', include('locations.urls')),
#     path('accounts/', include('allauth.urls')),
#     path('dj-rest-auth/', include('dj_rest_auth.urls')),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)