from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse_lazy
from django.http import JsonResponse
from check.models import *


class HomeView(TemplateView):
    template_name = 'home.html'


class UserRegisterView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    # 타이밍 로딩 문제로 reverse를 사용시 에러가 발생
    success_url = reverse_lazy('register_done')


class UserRegisterDoneView(TemplateView):
    template_name = 'registration/register_done.html'

def EventCount(request):
    user = request.user
    myEve = request.GET['eve']
    Event.objects.create(usr=user, event=myEve)
    laCount = Event.objects.filter(usr=user,event='LA').count()
    eaCount = Event.objects.filter(usr=user, event='EA').count()
    ouCount = Event.objects.filter(usr=user, event='OU').count()
    abCount = Event.objects.filter(usr=user, event='AB').count()
    result = {
        'la':laCount,
        'ea':eaCount,
        'ou':ouCount,
        'ab':abCount
    }
    return JsonResponse(result)
