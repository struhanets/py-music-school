from rest_framework import serializers

from musician.models import Musician


class MusicianSerializer(serializers.ModelSerializer):
    is_adult = serializers.ReadOnlyField()

    class Meta:
        model = Musician
        fields = (
            "id",
            "first_name",
            "last_name",
            "instrument",
            "age",
            "date_of_applying",
            "is_adult",
        )
        read_only_fields = ("id",)

    def create(self, validated_data):
        return Musician.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get(
            "first_name",
            instance.first_name
        )
        instance.last_name = validated_data.get(
            "last_name",
            instance.last_name
        )
        instance.instrument = validated_data.get(
            "instrument",
            instance.instrument
        )
        instance.age = validated_data.get("age", instance.age)
        instance.date_of_applying = validated_data.get(
            "date_of_applying",
            instance.date_of_applying
        )
        instance.save()
        return instance
