from django.shortcuts import render

# Create your views here.

from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView

from rest_framework import authentication,permissions

from Movie.serializers import MovieSerializer

from Movie.models import Movie


class MovieCreateView(CreateAPIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAdminUser]

    serializer_class = MovieSerializer

    def perform_create(self, serializer):

        serializer.save(created_by= self.request.user)

class movieListView(ListAPIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAuthenticated]

    serializer_class = MovieSerializer

    queryset = Movie.objects.all()    


#====================================MovieRetrive============================================================

class MovieRetrive(RetrieveAPIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAuthenticated]

    serializer_class = MovieSerializer

    queryset =  Movie.objects.all()    


#update,delete

class MovieUpdateDelete(UpdateAPIView,DestroyAPIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAdminUser]

    serializer_class = MovieSerializer

    queryset =  Movie.objects.all()  





    