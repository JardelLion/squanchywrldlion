from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GameViewSet, GoalViewSet

router = DefaultRouter()
router.register(r'games', GameViewSet)
router.register(r'goals', GoalViewSet)

urlpatterns = [
    path('', include(router.urls)),  # Inclui todas as URLs definidas pelo router
]
