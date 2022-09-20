from django.urls import path
from weddApp import views
from rest_framework.schemas import get_schema_view

urlpatterns = [
    path('', views.index),
        path('openapi', get_schema_view(
        title="Your Project",
        description="API for all things …"
    ), name='openapi-schema'),
]
