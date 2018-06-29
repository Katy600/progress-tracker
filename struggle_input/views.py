from django.urls import reverse_lazy
from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from struggle_input import views
from .models import StruggleData
from .forms import StruggleModelForm
import datetime
from django.urls import reverse
from django.template import RequestContext
from django.views.generic.edit import FormView
from django.views.generic.detail import DetailView
from django.utils import timezone
from django.views.generic.edit import UpdateView

from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render, reverse




def search(request):
  form = StruggleModelForm()
  errors = []
  struggles_in_progress = StruggleData.objects.filter(struggle_in_progess=True)

  if 'q' in request.GET:
    q = request.GET['q']
    if not q:
      errors.append('Enter a search term.')
    elif len(q) > 20:
      errors.append('Please enter at most 20 characters.')
    else:
      struggles = StruggleData.objects.filter(title__icontains=q)
      return render(request, 'struggle_input/struggle_form.html',{'struggles': struggles, 'query': q, 'form': form, 'searching': True, 'struggles_in_progress': struggles_in_progress })
  return render(request, 'struggle_input/struggle_form.html', {'errors': errors, 'form': form, 'searching': True,  'struggles_in_progress': struggles_in_progress})


class AddStruggle(FormView):
  form_class = StruggleModelForm
  template_name = 'struggle_input/struggle_form.html'
  success_url = reverse_lazy('struggles_input')

  def form_valid(self, form):
    # form = StruggleModelForm(request.POST, instance=a)
    form.save()
    return super().form_valid(form)

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    struggles_in_progress = StruggleData.objects.filter(struggle_in_progess=True)
    context['struggles_in_progress'] = struggles_in_progress
    return context


class DetailStruggleView(DetailView):
  model = StruggleData
  template_name = 'struggle_input/struggle-detail.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['now'] = timezone.now()
    return context

  def get_success_url(self):
    return reverse_lazy('struggle-detail', kwargs={'pk': self.get_object().id})


class CompleteStruggleFormView(UpdateView):
  model = StruggleData
  fields = ['title','time_started', 'time_ended', 'struggle', 'plan', 'frustration_level','code_screen_shot',  'learning_level', 'review_learning', 'struggle_in_progess', 'helpful_link', 'code_screen_shot_update']
  template_name = 'struggle_input/struggle-complete.html'
  # template_name_suffix = '_update_form'
  # success_url = reverse_lazy('struggle-complete')

  def get_success_url(self):
    return reverse_lazy('struggle-complete', kwargs={'pk': self.get_object().id})


  # def get_object(self, queryset=None):
  #   # get the existing object or created a new one
  #   obj, created = StruggleData.objects.get_or_create(col_1=self.kwargs['value_1'], col_2=self.kwargs['value_2'])
  #   print('obj', obj)
  #   print('created', created)
  #   return obj


# def my_view(request, pk): 
#   instance = StruggleData.objects.get(id=pk)
#   form = StruggleModelForm(request.POST or None, instance=instance)
#   if form.is_valid():
#     form.save()
#     return redirect('next_view')
#   return direct_to_template(request, 'struggle-detail.html', {'form': form})  

    # form_class = StruggleModelForm
    # template_name = 'struggle_input/struggle-detail.html'
    # success_url = reverse_lazy('struggles_input')

    # def form_valid(self, form):
    #     form = StruggleModelForm(request.POST, instance=struggles)
    #     form.save()
    #     # print("CompleteStruggleFormView", form)
    #     return super().form_valid(form)

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     struggles_in_progress = StruggleData.objects.filter(struggle_in_progess=True)
    #     context['struggles_in_progress'] = struggles_in_progress
    #     print("Context Complete", context)
    #     return context






# class CompleteStruggleFormView(UpdateView):
#     model = StruggleData
#     fields = ['time_ended', 'learning_level', 'review_learning', 'struggle_in_progess', 'helpful_link' ]
#     template_name_suffix = '_update_form'















