from django.urls import path

from Songs.views import SongsCreateview

from Songs.views import SongsListView,SongsRetriveView,SongsUpdateDeleteView

urlpatterns = [
    path('movie/<int:pk>/add/song/',SongsCreateview.as_view()),
    path('song/list/',SongsListView.as_view()),
    path('song/retrive/<int:pk>/',SongsRetriveView.as_view()),
    path('song/update/delete/<int:pk>/',SongsUpdateDeleteView.as_view()),
]
