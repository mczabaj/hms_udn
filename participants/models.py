from django.core.urlresolvers import reverse
from django.db import models

# Create your models here.
class Participant(models.Model):
    name = models.CharField(max_length=100, blank=False)
    age = models.CharField(max_length=3, blank=False)

    UMM_YES = "YES"
    SAY_NO = "NO"
    YES_NO_CHOICES = ((UMM_YES, 'Yes'), (SAY_NO, "No"))
    siblings = models.CharField(
        max_length=3,
        choices=YES_NO_CHOICES,
        default=SAY_NO)

    env_exposures = models.CharField(max_length=300, blank=True)
    genetic_mutations = models.CharField(max_length=300, blank=True)

    NOT_REVIEWED = 'NR'
    REVIEWED_ACCEPTED = 'RA'
    REVIEWED_NOT_ACCEPTED = 'RN'
    STATUS_CHOICES = (
        (NOT_REVIEWED, 'Not Reviewed'),
        (REVIEWED_ACCEPTED, 'Reviewed - Accepted'),
        (REVIEWED_NOT_ACCEPTED, 'Reviewed - Not Accepted'))
    status = models.CharField(
        max_length=2,
        choices=STATUS_CHOICES,
        default=NOT_REVIEWED)

    def __str__(self):
        return self.name
    def is_juvenile(self):
        return int(self.age) < 18

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})
