from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import ParticipantForm
from .models import Participant

class ParticipantCreate(CreateView):
    model = Participant
    fields = ['name', 'age', 'siblings', 'env_exposures', 'genetic_mutations']
    success_url = reverse_lazy('participants:index')

class ParticipantUpdate(UpdateView):
    model = Participant
    fields = ['name', 'age', 'siblings', 'env_exposures', 'genetic_mutations']
    success_url = reverse_lazy('participants:index')

class ParticipantDelete(DeleteView):
    model = Participant
    success_url = reverse_lazy('participants:index')

class ParticipantList(ListView):
    model = Participant
