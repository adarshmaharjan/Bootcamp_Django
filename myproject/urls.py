"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    # path('', forms_home),
    path('admin/', admin.site.urls),
    path('forms/', include('forms_practice.urls')),
    path('rest/', include('rest.urls')),
    path('static-demo/', include('static_media.urls')),
    path('api/', include('rest_class.urls')),
    path('crud/', include('crud.urls', namespace='crud'), ),
    path('classbased/', include('classbased.urls', namespace='classbased'))
]

if settings.DEBUG:
    urlpatterns += static('settings.MEDIA_URL',
                          document_root='settings.MEDIA_ROOT')
