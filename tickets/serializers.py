from rest_framework import serializers
from .models import Language, City, Movie, MoviesCityThrough

class LanguageSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()

    def create(self, validated_data):
        return Language.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance

class CitySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    language = serializers.PrimaryKeyRelatedField(queryset=Language.objects.all())
    seats = serializers.IntegerField()

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["language"] = instance.language.name
        return data

    def create(self, validated_data):
        return City.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance


class MovieSerialzer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    duration = serializers.FloatField()

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance
    


class MoviesCityThroughSerializer(serializers.Serializer):
    city = serializers.PrimaryKeyRelatedField(queryset=City.objects.all())
    movie = serializers.PrimaryKeyRelatedField(queryset=Movie.objects.all())
    m1 = serializers.BooleanField(required=False)
    m2 = serializers.BooleanField(required=False)
    a1 = serializers.BooleanField(required=False)
    a2 = serializers.BooleanField(required=False)
    e1 = serializers.BooleanField(required=False)
    e2 = serializers.BooleanField(required=False)
    e3 = serializers.BooleanField(required=False)
    amount =serializers.IntegerField()

    def create(self, validated_data):
        return MoviesCityThrough.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance


     

