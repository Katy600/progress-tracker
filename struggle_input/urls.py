from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from .views import AddStruggle, DetailStruggleView,  CompleteStruggleFormView
from django.urls import include, path
from . import views


urlpatterns = [

	path('struggles/input/',  AddStruggle.as_view(), name='struggles_input'),
	path('complete/', CompleteStruggleFormView.as_view(), name='complete'),
	path('complete/<int:pk>/', CompleteStruggleFormView.as_view(), name='struggle-complete'),
	path('delete/<int:pk>/',  AddStruggle.as_view(), name='struggle-delete'),
	path('struggles/<int:pk>/', DetailStruggleView.as_view(), name='struggle-detail'),
	url(r'^struggles/search$', views.search, name='struggles_search'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
