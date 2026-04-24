from django.contrib import admin

# Register your models here.
from .models import Team, Skill, TeamDependency, Meeting, TeamMember

admin.site.register(Team)
admin.site.register(Skill) 
admin.site.register(TeamDependency)
admin.site.register(Meeting)
admin.site.register(TeamMember)