from django.urls import path
from . import views

app_name = 'tripshit'

urlpatterns = [
    path('', views.home, name='home'),
    path('movies/', views.movies_list, name='movies_list'),
    path('movies/<int:movie_id>/', views.movie_detail, name='movie_detail'),
    
    path('characters/', views.characters_list, name='characters_list'),
    path('characters/<int:character_id>/', views.character_detail, name='character_detail'),
    
    path('starships/', views.starships_list, name='starships_list'),
    path('starships/<int:ship_id>/', views.starship_detail, name='starship_detail'),
]