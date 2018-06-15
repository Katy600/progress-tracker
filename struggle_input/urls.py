from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from .views import AddStruggle, DetailStruggleView
from django.urls import include, path
from . import views


urlpatterns = [
	path('<pk>/', DetailStruggleView.as_view(), name='struggle-detail'),
	url(r'^struggles/input$', AddStruggle.as_view(), name='struggles_input'),
	url(r'^struggles/search$', views.search, name='struggles_search'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
