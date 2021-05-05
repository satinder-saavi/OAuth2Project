from django.urls import path, include, re_path
from .views import (ExampleAuthentication, UserViewSet, UserProfileViewSet,
                    GroupViewSet
                    )
from rest_framework import routers, permissions
from rest_framework.schemas import get_schema_view
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# import rest_auth
# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'profile', UserProfileViewSet)
# router.register(r'groups', GroupViewSet)

schema_view = get_schema_view(
   openapi.Info(
      title="USER API",
      default_version='v1',
      description="User API Endpoints",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


# app_name="user-api"
urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('', include(router.urls)),
    path('rest-auth/', include('rest_auth.urls')),
    #  path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('api-token-auth/', ExampleAuthentication.as_view())
]
