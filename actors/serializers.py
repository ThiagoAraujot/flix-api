from rest_framework import serializers
from actors.models import Actor


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'

    def validate_birthday(self, value):
        if value.year < 1900:
            raise serializers.ValidationError(
                'Birthday must be after 1900')
        return value
