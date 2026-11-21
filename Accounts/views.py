from django.shortcuts import render

from rest_framework.views import APIView

from Accounts.serializers import AcountSerializer

from Accounts.models import User

from rest_framework.response import Response

from rest_framework import authentication,permissions

# Create your views here.
#-------------------------------------------------Admin-------------------------------------------------------------------

class AdminRegisterView(APIView):

    def post(self,request):

        form_data=request.data

        serializer_instance=AcountSerializer(data=form_data)

        if serializer_instance.is_valid():

            cleaned_data=serializer_instance.validated_data

            qs=User.objects.create_superuser(**cleaned_data,role="admin")

            serializerr_instance=AcountSerializer(qs)

            return Response(data=serializerr_instance.data)

        else:

            return Response(data=serializer_instance.errors)

#------------------------------------------User-----------------------------------------------------------------------------        

class userRegisterView(APIView):

    def post(self,request):

        form_data=request.data

        serializer_instance=AcountSerializer(data=form_data)

        if serializer_instance.is_valid():

            cleaned_data=serializer_instance.validated_data

            qs=User.objects.create_user(**cleaned_data)

            serializerr_instance=AcountSerializer(qs)

            return Response(data=serializerr_instance.data)

        else:

            return Response(data=serializer_instance.errors)  
    




