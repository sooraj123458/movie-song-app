from django.shortcuts import render

from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView

from rest_framework import authentication ,permissions

from Reviews.serializer import ReviewSerializer

from Reviews.models import Review

from Reviews.permissions import IsUser
# Create your views here.

class ReviewCreateView(CreateAPIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAuthenticated]

    serializer_class = ReviewSerializer

    def perform_create(self, serializer):

        serializer.save(created_by=self.request.user)

class ReviewListView(ListAPIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAuthenticated]

    serializer_class =  ReviewSerializer

    queryset = Review.objects.all()  


class ReviewRetriveView(RetrieveAPIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAuthenticated]

    serializer_class =  ReviewSerializer

    queryset = Review.objects.all()


class ReviewUpdateDeleteView(UpdateAPIView,DestroyAPIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [IsUser]

    serializer_class =  ReviewSerializer
    
    queryset = Review.objects.all()

    

