from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import routers, permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from apps.pessoas.urls import pessoas_router
from apps.pets.urls import pets_router
from apps.servicos.urls import servicos_router
from apps.pets.views import ListarPetsDoClienteView

router = routers.DefaultRouter()
router.registry.extend(pessoas_router.registry)
router.registry.extend(pets_router.registry)
router.registry.extend(servicos_router.registry)

schema_view = get_schema_view(
   openapi.Info(
      title="Documentação da Pet Happy API",
      default_version='v1',
      description="Backend do projeto Pet Happy",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('doc/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('', include(router.urls)),
    path('clientes/<int:pk>/pets/', ListarPetsDoClienteView.as_view()),
]
