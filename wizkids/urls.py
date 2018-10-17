"""wizkids URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views
from creator import views as creatorViews


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('accounts/', include('accounts.urls')),
    path('course/', include('feedbacks.urls')),
    path('creator/',include('creator.urls')),
    path('accd/',views.access_denied, name='accd'),
    path('listcourse/setvalue/',views.set_val, name='setvalue'),
    path('listcourse/',views.show_course, name='listc'),

    url(r'^/validate_username/$', creatorViews.validate_username, name='validate_username')
    
    # path('test/',views.show_test,name='learn')
    # all down is for pass reset
    # the previously added URL definitions
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
