from django.urls import path

from Movie.views import MovieCreateView,movieListView

from Movie.views import MovieRetrive,MovieUpdateDelete

urlpatterns = [
   path('add/',MovieCreateView.as_view()),
   path('list/',movieListView.as_view()),
   path('retr/<int:pk>/',MovieRetrive.as_view()),
   path('up/del/<int:pk>/',MovieUpdateDelete.as_view()),
]

