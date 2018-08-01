from django.urls import reverse_lazy
from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from struggle_input import views
from .models import StruggleData
from .forms import StruggleModelForm
import datetime
from django.utils import timezone
# from datetime import datetime, timedelta
from datetime import datetime, date
from django.urls import reverse
from django.template import RequestContext
from django.views.generic.edit import FormView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView

from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render, reverse


def search(request):
  errors = []
  if 'q' in request.GET:
    q = request.GET['q']
    if not q:
      errors.append('Enter a search term.')
    elif len(q) > 20:
      errors.append('Please enter at most 20 characters.')
    else:
      struggles = StruggleData.objects.filter(title__icontains=q).filter(struggle_in_progess=True)
      return render(request, 'struggle_input/struggle-list.html',{'struggles': struggles, 'query': q, 'searching': True })
  return render(request, 'struggle_input/struggle-list.html', {'errors': errors, 'searching': True})


class StruggleListView(ListView):
  model = StruggleData
  template_name = 'struggle_input/struggle-list.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['struggles'] = StruggleData.objects.all()

    return context


class AddStruggle(FormView):
  form_class = StruggleModelForm
  template_name = 'struggle_input/struggle_form.html'
  success_url = reverse_lazy('struggles_input')

  def form_valid(self, form):
    form.save()
    return super().form_valid(form)

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    struggles_in_progress = StruggleData.objects.filter(struggle_in_progess=False)
    context['struggles_in_progress'] = struggles_in_progress
    return context


class DetailStruggleView(DetailView):
  model = StruggleData
  template_name = 'struggle_input/struggle-detail.html'

  def get_times(self, **kwargs):
    time_started = kwargs['object'].time_started
    time_ended = kwargs['object'].time_ended
    return time_started, time_ended

  def get_duration(self, time):
    time_started, time_ended = time
    duration = time_ended - time_started
    return duration

  def convert_to_seconds(self, duration):
    seconds = duration.seconds
    return seconds

  def second_minute_hour(self, seconds):
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)

    return s, m, h

  def display_duration(self, **kwargs):
      time = self.get_times(**kwargs)
      duration = self.get_duration(time)
      seconds = self.convert_to_seconds(duration)
      return self.second_minute_hour(seconds)

  def get_context_data(self, **kwargs):
    s, m, h = self.display_duration(**kwargs)
    
    context = super().get_context_data(**kwargs)
    context['hour'] = h
    context['minute'] = m
    context['second'] = s
    context['now'] = timezone.now()
    return context

  def get_success_url(self):
    return reverse_lazy('struggle-detail', kwargs={'pk': self.get_object().id})


class CompleteStruggleFormView(UpdateView):
  model = StruggleData
  template_name = 'struggle_input/struggle-complete.html'
  form_class = StruggleModelForm

  def get_success_url(self):
    return reverse_lazy('struggles_input')