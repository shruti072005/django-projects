from django.urls import path
from .views import*

urlpatterns = [

   path('insert_player/',playerinsertview.as_view(), name='insert_player'),
   path('getone_player/',playerdetailview.as_view(), name='getone_player'),
   path('getall_player/',playergetallview.as_view(), name='getall_player'),
   path('allbat_player/',batsmanview.as_view(), name='allbat_player'),
   path('allball_player/',bowlerview.as_view(), name='allball_player'),
   path('getbyteam/',PlayersByTeamView.as_view(), name='getbyteam'),
   path('getbyname/',PlayersByNameView.as_view(), name='getbyname'),
   path('team_state/',TeamStatsView.as_view(), name='team_state'),
   path('teamview/',allteamsview.as_view(), name='teamview'),
   path('playerrank/',playerrankview.as_view(), name='playerrank'),
   path('playercount/',playercountview.as_view(), name='playercount'),
]
