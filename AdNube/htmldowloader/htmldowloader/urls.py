"""htmldowloader URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
# Django Inports
from django.urls import include, path
from django.contrib import admin

# Project Level Imports
from mainapp import views


# Third Party Imports
from rest_framework.routers import SimpleRouter


# intialize DefaultRouter
router = SimpleRouter()
# register accounts app urls with router
router.register(r'htmldowloader', views.UserViewSet, base_name='htmldowloader')




urlpatterns = [
    path(r'admin/', admin.site.urls),
    path('api/v1/', include((router.urls, 'api'), namespace='v1')),
]