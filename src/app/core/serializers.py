from rest_framework import serializers


class JokesSerializer(serializers.Serializer):
    jokes = serializers.ListField(read_only=True)

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)

    def create(self, validated_data):
        return super().create(validated_data)
