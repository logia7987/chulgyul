from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', Calendar.as_view(), name='calendar'),

]