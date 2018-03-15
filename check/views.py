from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import StudyClass,Student,Event


# Create your views here.
class Calendar(TemplateView):
    template_name = 'check/event_check.html'

    def get_context_data(self, **kwargs):
        user = self.request.user
        info = Student.objects.get(stu=user)
        info = info.group
        dayinfo = StudyClass.objects.get(studyclass=info)
        context = super().get_context_data(**kwargs)
        context['user'] = user
        context['info'] = info
        context['dayinfo'] = dayinfo
        context['late'] = Event.objects.filter(usr=user, event='LA').count()
        context['early'] = Event.objects.filter(usr=user, event='EA').count()
        context['absen'] = Event.objects.filter(usr=user, event='AB').count()
        context['out'] = Event.objects.filter(usr=user, event='OU').count()
        return context


