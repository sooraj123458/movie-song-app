from rest_framework import serializers

from Songs.models import Song

class Songserializer(serializers.ModelSerializer):

    created_by = serializers.StringRelatedField()

    movie = serializers.StringRelatedField()

    class Meta:

        model = Song

        fields = "__all__"

        read_only_fields = ["id","track_number","created_at","updated_at","movie","created_by"]


            
            