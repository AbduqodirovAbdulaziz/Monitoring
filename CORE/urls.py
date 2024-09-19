from django.contrib import admin
from django.urls import path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from mainApp.views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    path('xaridor/', XaridorApiView.as_view()),
    path('xaridor/<int:pk>/', XaridorEditApiView.as_view()),

    path('sotuv/', SotuvApiView.as_view()),
    path('sotuv/<int:pk>/', SotuvEdit.as_view()),

    path('xarajat/', XarajatlarApiView.as_view()),
    path('xarajat/<int:pk>/', XarajatlarEditApiView.as_view()),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
