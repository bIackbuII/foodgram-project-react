from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import IngredientsViewSet
from .views import RecipeViewSet
from .views import TagsViewSet

router = DefaultRouter()
router.register('recipes', RecipeViewSet, basename='recipes')
router.register('ingredients', IngredientsViewSet, basename='ingredients')
router.register('tags', TagsViewSet, basename='tags')

urlpatterns = [
    path('', include(router.urls)),
]
