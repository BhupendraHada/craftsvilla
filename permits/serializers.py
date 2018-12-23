from rest_framework import serializers
from .models import FoodFacilityPermits


class FoodFacilityPermitsSerializer(serializers.ModelSerializer):

    class Meta:
        model = FoodFacilityPermits

    def create(self, validated_data):
        validated_data['created_by'] = self.context['request'].user
        validated_data['modified_by'] = self.context['request'].user
        return FoodFacilityPermits.objects.create(**validated_data)

    def update(self, instance, validated_data):
        validated_data['modified_by'] = self.context['request'].user
        return super(OutletSerializer, self).update(instance, validated_data)
