from django.urls import path

from Accounts.views import AdminRegisterView

from Accounts.views import userRegisterView

from rest_framework.authtoken.views import ObtainAuthToken

urlpatterns = [
   path('register/',AdminRegisterView.as_view()),
   path('user/register/',userRegisterView.as_view()),
   path('token/',ObtainAuthToken.as_view()),
]