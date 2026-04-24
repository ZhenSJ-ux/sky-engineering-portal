from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.core.mail import send_mail
from .models import Team, Meeting
from .forms import EmailTeamForm, MeetingForm

def about(request):
    return render(request, 'about.html', {
        'page_title': 'About',
    })


def team_list(request):
    query = request.GET.get('q', '')
    teams = Team.objects.all()

    if query:
        teams = teams.filter(
            Q(name__icontains=query) |
            Q(manager_name__icontains=query) |
            Q(department__icontains=query)
        )

    return render(request, 'team_list.html', {
        'teams': teams,
        'query': query,
        'page_title': 'Teams',
    })


def team_detail(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    return render(request, 'team_detail.html', {
        'team': team,
        'page_title': team.name,
    })
def email_team(request, team_id):
    team = get_object_or_404(Team, id=team_id)

    if request.method == 'POST':
        form = EmailTeamForm(request.POST)
        if form.is_valid():
            send_mail(
                form.cleaned_data['subject'],
                form.cleaned_data['message'],
                'test@example.com',
                [team.manager_email],
                fail_silently=False,
            )
            return redirect('team_detail', team_id=team.id)
    else:
        form = EmailTeamForm()

    return render(request, 'email_team.html', {
        'team': team,
        'form': form,
    })


def schedule_meeting(request, team_id):
    team = get_object_or_404(Team, id=team_id)

    if request.method == 'POST':
        form = MeetingForm(request.POST)
        if form.is_valid():
            meeting = form.save(commit=False)
            meeting.team = team
            meeting.save()
            return redirect('team_detail', team_id=team.id)
    else:
        form = MeetingForm()

    return render(request, 'schedule_meeting.html', {
        'team': team,
        'form': form,
    })



def home(request):
    team_count = Team.objects.count()
    meeting_count = Meeting.objects.count()

    return render(request, 'home.html', {
        'team_count': team_count,
        'meeting_count': meeting_count
    })

def team_members(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    return render(request, 'team_members.html', {
        'team': team,
        'page_title': f'{team.name} Members',
    })
