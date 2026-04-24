
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('teams/', views.team_list, name='team_list'), #added
    path('teams/<int:team_id>/', views.team_detail, name='team_detail'),
    path('teams/<int:team_id>/email/', views.email_team, name='email_team'),
    path('teams/<int:team_id>/schedule/', views.schedule_meeting, name='schedule_meeting'),
]