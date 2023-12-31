"""
URL configuration for spotify project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path, include
from asosiy.views import *
from drf_spectacular.views import SpectacularSwaggerView, SpectacularRedocView, SpectacularAPIView

router = DefaultRouter()
router.register("albomlar" , AlbomModelViewSet )
router.register("qoshiqlar" , QoshiqModelViewSet)
router.register("qoshiqchilar" , QoshiqchiModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('apiview_docs/', SpectacularAPIView.as_view(), name="schema"),
    path('docs/', SpectacularSwaggerView.as_view(url_name="schema")),
    path('redoc/', SpectacularRedocView.as_view(url_name="schema")),
    # path('qoshiqchilar/', QoshiqchilarAPIView.as_view()),
    # path('qoshiqchi/<int:pk>/', QoshiqchiDetalView.as_view()),
    # path('qoshiq/<int:pk>/', QoshiqDetalView.as_view()),
]
