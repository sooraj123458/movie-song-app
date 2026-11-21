from django.urls import path

from Reviews.views import ReviewCreateView,ReviewListView,ReviewRetriveView,ReviewUpdateDeleteView

urlpatterns = [
    path('add/',ReviewCreateView.as_view()),
    path('list/',ReviewListView.as_view()),
    path('retrive/<int:pk>/',ReviewRetriveView.as_view()),
    path('update/delete/<int:pk>/',ReviewUpdateDeleteView.as_view()),
    
]