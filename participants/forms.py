from django import forms

class ParticipantForm(forms.ModelForm):
    name = forms.CharField(max_length=100, required=True)
    age = forms.CharField(max_length=3, required=True)
    UMM_YES = "YES"
    SAY_NO = "NO"
    YES_NO_CHOICES = ((UMM_YES, 'Yes'), (SAY_NO, "No"))
    siblings = forms.CharField(max_length=3,
                               widget=forms.Select(choices=YES_NO_CHOICES))
    env_exposures = forms.CharField(widget=forms.Textarea(attrs={'max_length':300, 'required':False}))
    genetic_mutations = forms.CharField(widget=forms.Textarea,
                                        max_length=300,
                                        required=False)

    NOT_REVIEWED = 'NR'
    REVIEWED_ACCEPTED = 'RA'
    REVIEWED_NOT_ACCEPTED = 'RN'
    STATUS_CHOICES = (
        (NOT_REVIEWED, 'Not Reviewed'),
        (REVIEWED_ACCEPTED, 'Reviewed - Accepted'),
        (REVIEWED_NOT_ACCEPTED, 'Reviewed - Not Accepted'))
    status = forms.CharField(max_length=2,
                             widget=forms.Select(choices=STATUS_CHOICES))

    def create_participant(self):
        pass
    def update_participant(self):
        pass
