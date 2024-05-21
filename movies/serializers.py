from django.db.models import Avg
from rest_framework import serializers
from movies.models import Movies


class MoviesSerializer(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movies
        fields = '__all__'

    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']

        if rate:
            return round(rate, 1)

        return None

    def validate_release_date(self, value):
        if value.year < 1900:
            raise serializers.ValidationError(
                'Release date must be after 1970')
        return value

    def validate_resume(self, value):
        if len(value) > 1000:
            raise serializers.ValidationError(
                'Resume must have less than 1000 characters')
        return value
