from django.shortcuts import render,get_object_or_404

# Create your views here.

from rest_framework.views import APIView

from Movie.models import Movie

from Movie.serializers import MovieSerializer

from rest_framework import authentication,permissions

from rest_framework.response import Response

from Songs.serializers import Songserializer

from rest_framework.generics import ListAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView

from Songs.models import Song


class SongsCreateview(APIView):

    authentication_classes=[authentication.TokenAuthentication]

    permission_classes=[permissions.IsAdminUser]

    def post(self,request,pk=None):

        movie_id=pk

        #movie_object=Movie.objects.get(id=movie_id)

        movie_object=get_object_or_404(Movie,id=movie_id)

        form_data=request.data

        serializer_instance=Songserializer(data=form_data)

        if serializer_instance.is_valid():

            serializer_instance.save(movie=movie_object,created_by=request.user)

            return Response(data=serializer_instance.data)

        else:

            return Response(data=serializer_instance.errors)

#------------------------------------------list----------------------------------        

class SongsListView(ListAPIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAuthenticated]

    serializer_class = Songserializer

    queryset = Song.objects.all() 

#==================================================retrive======================================================

class SongsRetriveView(RetrieveAPIView):

    authentication_classes = [authentication.TokenAuthentication]
    
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = Songserializer

    queryset = Song.objects.all() 


#============================================update-delete======================================================

class SongsUpdateDeleteView(UpdateAPIView,DestroyAPIView):

    authentication_classes = [authentication.TokenAuthentication]
        
    permission_classes = [permissions.IsAdminUser]

    serializer_class = Songserializer

    queryset = Song.objects.all()








