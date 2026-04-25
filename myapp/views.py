# imports Django shortcuts for rendering pages, finding objects, and redirecting users
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q # imports Q to allow advanced search using OR conditions
from django.core.mail import send_mail # imports Django email function
from .models import Team, Meeting # imports database models
from .forms import EmailTeamForm, MeetingForm # imports forms used for email and meetings


# displays the about page
def about(request):
    return render(request, 'about.html', {
        'page_title': 'About',  # sets page title
    })


# displays all teams and handles search
def team_list(request):
    query = request.GET.get('q', '')  # gets search query from URL

    teams = Team.objects.all()  # gets all teams from database

    # filters teams if user searched something
    if query:
        teams = teams.filter(
            Q(name__icontains=query) |  # searches team name
            Q(manager_name__icontains=query) |  # searches manager name
            Q(department__icontains=query)  # searches department
        )

    # sends teams and search query to template
    return render(request, 'team_list.html', {
        'teams': teams,
        'query': query,
        'page_title': 'Teams',
    })


# displays details for one specific team
def team_detail(request, team_id):
    team = get_object_or_404(Team, id=team_id)  # gets team or shows 404 if not found

    return render(request, 'team_detail.html', {
        'team': team,
        'page_title': team.name,
    })


# handles sending an email to a team manager
def email_team(request, team_id):
    team = get_object_or_404(Team, id=team_id)  # gets selected team

    # checks if form has been submitted
    if request.method == 'POST':
        form = EmailTeamForm(request.POST)  # fills form with submitted data

        # checks form validation
        if form.is_valid():
            send_mail(
                form.cleaned_data['subject'],  # email subject
                form.cleaned_data['message'],  # email message
                'test@example.com',  # sender email
                [team.manager_email],  # recipient email
                fail_silently=False,  # show error if email fails
            )

            # redirects back to team detail page after sending
            return redirect('team_detail', team_id=team.id)

    else:
        form = EmailTeamForm()  # creates empty form for GET request

    # displays email form page
    return render(request, 'email_team.html', {
        'team': team,
        'form': form,
    })


# handles scheduling a meeting for a team
def schedule_meeting(request, team_id):
    team = get_object_or_404(Team, id=team_id)  # gets selected team

    # checks if meeting form was submitted
    if request.method == 'POST':
        form = MeetingForm(request.POST)  # fills form with submitted data

        # checks form is valid
        if form.is_valid():
            meeting = form.save(commit=False)  # creates meeting object but does not save yet
            meeting.team = team  # links meeting to selected team
            meeting.save()  # saves meeting to database

            # redirects back to team detail page
            return redirect('team_detail', team_id=team.id)

    else:
        form = MeetingForm()  # creates empty form

    # displays meeting form page
    return render(request, 'schedule_meeting.html', {
        'team': team,
        'form': form,
    })


# displays dashboard/home page
def home(request):
    team_count = Team.objects.count()  # counts total teams
    meeting_count = Meeting.objects.count()  # counts total meetings

    # sends dashboard counts to template
    return render(request, 'home.html', {
        'team_count': team_count,
        'meeting_count': meeting_count
    })


# displays members for a selected team
def team_members(request, team_id):
    team = get_object_or_404(Team, id=team_id)  # gets selected team

    return render(request, 'team_members.html', {
        'team': team,
        'page_title': f'{team.name} Members',
    })