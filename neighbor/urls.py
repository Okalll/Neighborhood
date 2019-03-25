from django.conf.urls import url
from . import views
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^$',views.home, name='home'),
    url(r'signup', views.signup, name='signup'),
    url(r'^new_hood/', views.new_hood, name='new_hood'),
    url(r'^profile/', views.profile, name='profile'),
    url(r'^update_profile/', views.update_profile, name='update_profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


