"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
import debug_toolbar
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication


schema_view = get_schema_view(
    openapi.Info(
        title='Hotels API',
        description='our description',
        default_version='v1',
        terms_of_service='https://hotels.com',
        contact=openapi.Contact(email='makarenkoek@yandex.ru'),
        license=openapi.License(name='License')
    ),
    public=True,
    permission_classes=[permissions.AllowAny, ],
    authentication_classes=[TokenAuthentication, ]
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hotel.urls')),
    path('', include('comment.urls')),
    path('api/', include([
        path('', include('hotel_rest.urls')),
        path('', include('authentication.urls')),
        path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-ui'),
        path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc-ui')
    ])),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls))
    ]
