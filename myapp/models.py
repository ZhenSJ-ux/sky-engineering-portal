from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    manager_name = models.CharField(max_length=100)
    manager_email = models.EmailField()
    purpose = models.TextField(blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='skills')

    def __str__(self):
        return self.name


class TeamDependency(models.Model):
    from_team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        related_name='outgoing_dependencies'
    )
    to_team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        related_name='incoming_dependencies'
    )

    def __str__(self):
        return f"{self.from_team} → {self.to_team}"


class Meeting(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='meetings')
    title = models.CharField(max_length=150)
    date = models.DateField()
    time = models.TimeField()
    platform = models.CharField(max_length=100, blank=True)
    message = models.TextField(blank=True)

    def __str__(self):
        return f"{self.title} ({self.team.name})"
        

class TeamMember(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='members')
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.name} ({self.team.name})"

