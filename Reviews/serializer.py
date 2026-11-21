from rest_framework import serializers

from Reviews.models import Review

class ReviewSerializer(serializers.ModelSerializer):

    created_by = serializers.StringRelatedField()

    class Meta:

        model = Review

        fields = "__all__"

        read_only_fields = ["id","created_by","created_at","updated_at"]