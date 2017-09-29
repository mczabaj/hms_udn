from django import forms

class ParticipantForm(forms.ModelForm):
    name = forms.CharField(max_length=100, required=True)
    age = forms.CharField(max_length=3, required=True)
    UMM_YES = "YES"
    SAY_NO = "NO"
    YES_NO_CHOICES = ((UMM_YES, 'Yes'), (SAY_NO, "No"))
    siblings = forms.CharField(max_length=3,
                               widget=forms.Select(choices=YES_NO_CHOICES))
    env_exposures = forms.CharField(max_length=300,
                                    widget=forms.Textarea,
                                    required=False)
    genetic_mutations = forms.CharField(max_length=300,
                                        widget=forms.Textarea,
                                        required=False)

    def create_participant(self):
        pass
    def update_participant(self):
        pass
