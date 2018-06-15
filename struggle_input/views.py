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


def search(request):
	form = StruggleModelForm()
	errors = []
	if 'q' in request.GET:
		q = request.GET['q']
		if not q:
			errors.append('Enter a search term.')
		elif len(q) > 20:
			errors.append('Please enter at most 20 characters.')
		else:
			struggles = StruggleData.objects.filter(title__icontains=q)
			return render(request, 'struggle_input/struggle_form.html',{'struggles': struggles, 'query': q, 'form': form, 'searching': True})
	return render(request, 'struggle_input/struggle_form.html', {'errors': errors, 'form': form, 'searching': True})


class AddStruggle(FormView):
    form_class = StruggleModelForm
    template_name = 'struggle_input/struggle_form.html'
    success_url = reverse_lazy('struggles_input')

    def form_valid(self, form):
    	form.save()
    	return super().form_valid(form)







