from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import routers

from pessoas.urls import pessoas_router
from pets.urls import pets_router
from pets.views import ListarPetsDoClienteView

router = routers.DefaultRouter()
router.registry.extend(pessoas_router.registry)
router.registry.extend(pets_router.registry)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('', include(router.urls)),
    path('clientes/<int:pk>/pets/', ListarPetsDoClienteView.as_view()),
]
