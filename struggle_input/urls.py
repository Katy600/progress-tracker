from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from .views import AddStruggle
from . import views

urlpatterns = [
	# url(r'^search/$', views.search),
	# url(r'^struggles/$', views.add_struggle),
	# url(r'^search/$', views.search),
	url(r'^struggles/input$', AddStruggle.as_view(), name='struggles_input'),
	url(r'^struggles/search$', views.search, name='struggles_search'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



# ###urls.py###
# url(r'^$', views.landing.as_view(), name = 'landing'),

# ####views.py####
# class landing(View):
#     template_name = '/home.html'
#     form_class1 = forms.pynamehere1
#     form_class2 = forms.pynamehere2
#         def get(self, request):
#             form1 = self.form_class1(None)
#             form2 = self.form_class2(None)
#             return render(request, self.template_name, { 'register':form1, 'login':form2,})

#          def post(self, request):
#              if request.method=='POST' and 'htmlsubmitbutton1' in request.POST:
#                     ## do what ever you want to do for first function ####
#              if request.method=='POST' and 'htmlsubmitbutton2' in request.POST:
#                      ## do what ever you want to do for second function ####
#                     ## return def post###  
#              return render(request, self.template_name, {'form':form,})


# ####/home.html####
# #### form 1 ####
# <form action="" method="POST" >
#   {% csrf_token %}
#   {{ register.as_p }}
# <button type="submit" name="htmlsubmitbutton1">Login</button>
# </form>
# #### form 2 ####
# <form action="" method="POST" >
#   {% csrf_token %}
#   {{ login.as_p }}
# <button type="submit" name="htmlsubmitbutton2">Login</button>
# </form>