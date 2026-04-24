from django import forms
from .models import Meeting

class EmailTeamForm(forms.Form):
    subject = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={'placeholder': 'Email subject'})
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Write your message...'})
    )

class MeetingForm(forms.ModelForm):

    TIME_CHOICES = [
        ('09:00', '09:00 AM'),
        ('10:00', '10:00 AM'),
        ('11:00', '11:00 AM'),
        ('12:00', '12:00 PM'),
        ('13:00', '13:00 PM'),
        ('14:00', '14:00 PM'),
        ('15:00', '15:00 PM'),
        ('16:00', '16:00 PM'),
        ('17:00', '17:00 PM'),
        ('18:00', '18:00 PM'),
        ('19:00', '19:00 PM'),
        ('20:00', '20:00 PM'),
        ('21:00', '21:00 PM'),
        ('22:00', '22:00 PM'),
    ]

    time = forms.ChoiceField(choices=TIME_CHOICES)
    
    class Meta:
        model = Meeting
        fields = ['title', 'date', 'time', 'platform', 'message']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Meeting title'}),
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TextInput(attrs={'placeholder': 'e.g. 14:30'}),
            'platform': forms.TextInput(attrs={'placeholder': 'Zoom / Teams / Google Meet'}),
            'message': forms.Textarea(attrs={'placeholder': 'Agenda or message'}),
        }