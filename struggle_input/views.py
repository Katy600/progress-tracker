from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from struggle_input import views
from .models import StruggleData
from .forms import StruggleForm
import datetime
from django.urls import reverse


def hello(request):
    return HttpResponse("Hello world")


def search(request):
	errors = []
	if 'q' in request.GET:
		q = request.GET['q']
		if not q:
			errors.append('Enter a search term.')
		elif len(q) > 20:
			errors.append('Please enter at most 20 characters.')
		else:
			struggles = StruggleData.objects.filter(title__icontains=q)
			return render(request, 'struggle_input/search_results.html',{'struggles': struggles, 'query': q})
	return render(request, 'struggle_input/search_form.html', {'errors': errors})


def add_struggle(request):
    if request.method == 'POST':
        form = StruggleForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data['date']
            title = form.cleaned_data['title']
            struggle = form.cleaned_data['struggle']
            plan = form.cleaned_data['plan']
            frustration_level = form.cleaned_data['frustration_level']
            time_off_task = form.cleaned_data['time_off_task']
            code_screen_shot = form.cleaned_data['code_screen_shot']

            struggle_data = StruggleData.objects.create(
            									 title=title,
            									 date=date,
            									 struggle=struggle, 
            									 plan=plan, 
            									 frustration_level=frustration_level,
            									 time_off_task=time_off_task,
            									 code_screen_shot=code_screen_shot,
                                         		)
            return HttpResponseRedirect('/struggles')
    else:
        form = StruggleForm()

    return render(request, 'struggle_input/struggle_form.html', {'form': form})








