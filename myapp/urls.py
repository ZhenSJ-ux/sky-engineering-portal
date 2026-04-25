
from django.urls import path # imports path function to define URL routes
from . import views # imports views file where functions are written

urlpatterns = [
    path('', views.home, name='home'), # home page (dashboard)
    path('teams/', views.team_list, name='team_list'), # team list page (shows all teams + search)
    path('teams/<int:team_id>/', views.team_detail, name='team_detail'), # team detail page (uses team_id to show specific team)
    path('teams/<int:team_id>/email/', views.email_team, name='email_team'), # email team page (form to send email to team manager)
    path('teams/<int:team_id>/schedule/', views.schedule_meeting, name='schedule_meeting'), # schedule meeting page (form to create meeting)
    path('teams/<int:team_id>/members/', views.team_members, name='team_members'),  # team members page (shows all members in a team)
]