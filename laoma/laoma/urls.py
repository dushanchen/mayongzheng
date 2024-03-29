"""laoma URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
import os
from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from finance import views as f 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ueditor/', include('DjangoUeditor.urls')),

    path('', f.index),
    path('index/', f.index),
    path('xintuo/', f.xintuo),
    path('dingrong/', f.dingrong),
    path('news/', f.news),
    path('article/<int:id>/', f.article),
    path('article/<int:id>/', f.article),
    path('article/<int:id>/', f.article),

] 

if settings.DEBUG:
    media_root = os.path.join(settings.BASE_DIR, settings.MEDIA_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=media_root)

