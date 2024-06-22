from django.urls import path
from .viewsets import LanguageViewSet, CityViewSet, MovieViewSet

urlpatterns = [
    path("language/", LanguageViewSet.as_view({"post": "create", "get": "list"})),

    path("city/", CityViewSet.as_view({"post": "create", "get": "list"})),
    path("city/<int:city_id>/", CityViewSet.as_view({"delete": "delete", "patch": "update"})),

    path("movie/", MovieViewSet.as_view({"post": "create", "get": "list"})),
    path("movie/<int:movie_id>/", MovieViewSet.as_view({"patch": "update"})),

    
]