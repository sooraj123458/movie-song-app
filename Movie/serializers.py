from rest_framework import serializers

from Movie.models import Movie

from Songs.models import Song

from Songs.serializers import Songserializer

class MovieSerializer(serializers.ModelSerializer):

    created_by = serializers.StringRelatedField()

    total_songs = serializers.SerializerMethodField(read_only=True)

    songs = serializers.SerializerMethodField(read_only=True)

    class Meta:

        model = Movie

        fields = "__all__"

        read_only_fields = ["id","created_by","created_at","updated_at"]

    def get_total_songs(self,obj):

        return  Song.objects.filter(movie=obj).count()

    def get_songs(self,obj):

        songs_object=Song.objects.filter(movie=obj)

        serializer_instance=Songserializer(songs_object,many=True)

        return  serializer_instance.data

