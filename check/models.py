from django.db import models

# Create your models here.
class Event(models.Model):
    LATE = 'LA'
    EARLY = 'EA'
    ABSEN = 'AB'
    OUT = 'OU'
    EVENT_CHOICE = (
        (LATE, '지각'),
        (EARLY, '조퇴'),
        (ABSEN, '결석'),
        (OUT, '외출'),
    )
    event = models.CharField(
        max_length=2,
        choices=EVENT_CHOICE
    )
    usr = models.ForeignKey('auth.User')
    event_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.event

class StudyClass(models.Model):
    CLASS202 = '202'
    CLASS203 = '203'
    CLASS_CHOICE = (
        (CLASS202,'202반'),
        (CLASS203, '203반')
    )
    studyclass = models.CharField(
        max_length=3,
        choices=CLASS_CHOICE
    )
    unit = models.PositiveIntegerField()
    limit = models.PositiveIntegerField()

    def __str__(self):
        return self.studyclass

class Student(models.Model):
    stu = models.ForeignKey('auth.User')
    group = models.ForeignKey(StudyClass)

    def __str__(self):
        return self.stu.username
