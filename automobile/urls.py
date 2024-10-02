"""
URL configuration for automobile project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from am.views import index, cardetails,signup, login_view, user_logout
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index, name="index"),
    path('cardetails/<int:car_id>/', cardetails, name="cardetails"),
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('/logout', user_logout, name='logout')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
