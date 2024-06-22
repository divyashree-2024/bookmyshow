from rest_framework.viewsets import ViewSet
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from .serializers import LanguageSerializer, CitySerializer, MovieSerialzer, MoviesCityThroughSerializer
from .models import Language, City, Movie, MoviesCityThrough, Ticket

class LanguageViewSet(ViewSet, ListAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    authentication_classes = ()
    permission_classes = ()

    def create(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        if not serializer.is_valid():
            return Response(data=serializer.errors, status=HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(data=serializer.data, status=HTTP_200_OK)
    
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    

class CityViewSet(ViewSet, ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    authentication_classes = ()
    permission_classes = ()

    def create(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        if not serializer.is_valid():
            return Response(data=serializer.errors, status=HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(data=serializer.data, status=HTTP_200_OK)
    
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    def update(self, request, city_id):
        data = request.data
        city = self.queryset.filter(pk=city_id)
        if not city:
            return Response(data={"error": "invalid city_id"}, status=HTTP_400_BAD_REQUEST)
        serializer = self.serializer_class(instance=city.last(), data=data, partial=True)
        if not serializer.is_valid():
            return Response(data=serializer.errors, status=HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(data=serializer.data, status=HTTP_200_OK)
    
    def delete(self, city_id):
        city = self.queryset.filter(pk=city_id)
        if not city:
            return Response(data={"error": "invalid city_id"}, status=HTTP_400_BAD_REQUEST)
        city.delete()
        return Response(data={}, status=HTTP_200_OK)
    

class MovieViewSet(ViewSet, ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerialzer
    authentication_classes = ()
    permission_classes = ()

    def create(self, request):
        data = request.data
        city_movie_data = data.pop("cities", {}) 
        movie_serializer = self.serializer_class(data=data)
        if not movie_serializer.is_valid():
            return Response(data=movie_serializer.errors, status=HTTP_400_BAD_REQUEST)
        movie = movie_serializer.save()

        for i in city_movie_data:
            i["movie"] = movie.id
        city_movie_serializer = MoviesCityThroughSerializer(data=city_movie_data, many=True)
        if not city_movie_serializer.is_valid():
            return Response(data=city_movie_serializer.errors, status=HTTP_400_BAD_REQUEST)

        city_movie_serializer.save()
        response_data = {
            "cities": city_movie_serializer.data
        }
        response_data.update(movie_serializer.data)
        return Response(data=response_data, status=HTTP_200_OK)

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    def update(self, request, movie_id):
        data = request.data
        movie = self.queryset.filter(pk=movie_id)
        if not movie:
            return Response(data={"error": "invalid movie_id"}, status=HTTP_400_BAD_REQUEST)
        serializer = self.serializer_class(instance=movie.last(), data=data, partial=True)
        if not serializer.is_valid():
            return Response(data=serializer.errors, status=HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(data=serializer.data, status=HTTP_200_OK)
    
    def delete(self, movie_id):
        movie = self.queryset.filter(pk=movie_id)
        if not movie:
            return Response(data={"error": "invalid movie_id"}, status=HTTP_400_BAD_REQUEST)
        movie.delete()
        return Response(data={}, status=HTTP_200_OK)
    