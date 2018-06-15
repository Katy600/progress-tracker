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


# def add_struggle(request):
#     if request.method == 'POST':
#         form = StruggleModelForm(request.POST, request.FILES)
#         print(form)
#         if form.is_valid():
#             date = form.cleaned_data['date']
#             title = form.cleaned_data['title']
#             struggle = form.cleaned_data['struggle']
#             plan = form.cleaned_data['plan']
#             frustration_level = form.cleaned_data['frustration_level']
#             time_off_task = form.cleaned_data['time_off_task']
#             code_screen_shot = form.cleaned_data['code_screen_shot']
      
#             struggle_data = StruggleData.objects.create(
#             									 title=title,
#             									 date=date,
#             									 struggle=struggle, 
#             									 plan=plan, 
#             									 frustration_level=frustration_level,
#             									 time_off_task=time_off_task,
#             									 code_screen_shot= request.FILES['code_screen_shot']
#                                          		)
#             return HttpResponseRedirect('/struggles')
#     else:
#         form = StruggleModelForm()

#     return render(request, 'struggle_input/struggle_form.html', {'form': form})


class AddStruggle(FormView):
    form_class = StruggleModelForm
    template_name = 'struggle_input/struggle_form.html'
    success_url = reverse_lazy('struggles_input')

    # def get(self, request, *args, **kwargs):
    #     form = self.form_class(initial=self.initial)
    #     return render(request, self.template_name, {'form': form})

    # def post(self, request, *args, **kwargs):
    #     form = self.form_class(request.POST)
    #     if form.is_valid():
    #         # <process form cleaned data>
    #         return HttpResponseRedirect('/struggles/')

        # return render(request, self.template_name, {'form': form})

    def form_valid(self, form):
    	form.save()
    	return super().form_valid(form)







