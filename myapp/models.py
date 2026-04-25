# imports Django model system
from django.db import models


# team model

class Team(models.Model):
    name = models.CharField(max_length=100)  # team name
    department = models.CharField(max_length=100)  # department name
    manager_name = models.CharField(max_length=100)  # team manager name
    manager_email = models.EmailField()  # manager email (validated format)
    purpose = models.TextField(blank=True)  # optional purpose of team
    description = models.TextField(blank=True)  # optional description

    def __str__(self):
        return self.name  # readable name in admin / queries


# skill model

class Skill(models.Model):
    name = models.CharField(max_length=100)  # skill name

    # foreign key linking skill to a team (many skills per team)
    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,  # delete skills if team is deleted
        related_name='skills'  # allows access via team.skills.all()
    )

    def __str__(self):
        return self.name


# team dependency model

class TeamDependency(models.Model):

    # team that depends on another team (source)
    from_team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        related_name='outgoing_dependencies'  # access via team.outgoing_dependencies
    )

    # team being depended on (target)
    to_team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        related_name='incoming_dependencies'  # access via team.incoming_dependencies
    )

    def __str__(self):
        return f"{self.from_team} → {self.to_team}"  # readable relationship


# meeting model

class Meeting(models.Model):

    # links meeting to a team (one team can have many meetings)
    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        related_name='meetings'  # access via team.meetings.all()
    )

    title = models.CharField(max_length=150)  # meeting title
    date = models.DateField()  # meeting date
    time = models.TimeField()  # meeting time
    platform = models.CharField(max_length=100, blank=True)  # optional platform (Zoom, Teams)
    message = models.TextField(blank=True)  # optional meeting details

    def __str__(self):
        return f"{self.title} ({self.team.name})"


# team member model

class TeamMember(models.Model):

    # links member to a team (one team → many members)
    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        related_name='members'  # access via team.members.all()
    )

    name = models.CharField(max_length=100)  # member name
    role = models.CharField(max_length=100)  # role in team
    occupation = models.CharField(max_length=100, blank=True)  # optional job title

    def __str__(self):
        return f"{self.name} ({self.team.name})"
