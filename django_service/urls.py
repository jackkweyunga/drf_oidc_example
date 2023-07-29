from django.contrib import admin
from django.urls import path, include

from django_service.views import HealCheck
from exampleapp.views import Index, IndexProtected

urlpatterns = [

    path('oidc/', include('mozilla_django_oidc.urls')),

    #     healthcheck endpoint
    path("healthcheck/", HealCheck.as_view(), name="healthcheck"),

    #     default base endpoint
    path("", Index.as_view(), name="default-base-endpoint"),
    path("protected/", IndexProtected.as_view(), name="default-protected-base-endpoint")

]
