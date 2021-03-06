from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.timezone import now
from datetime import datetime


CATEGORIES = (
    ('ELE', 'Electric'),
    ('PLU', 'Plumbing'),
    ('LIG', 'Light fixtures'),
    ('HAC', 'Heating - AC'),
    ('ELV', 'Elevators'),
    ('DOR', 'Doors & Locks'),
    ('WIN', 'Windows'),
    ('FLR', 'Floors'),
    ('EXT', 'Exterminator'),
    ('OTR', 'Other'),
)

PRIORITIES = (
    ('L', 'LOW'),
    ('M', 'MEDIUM'),
    ('H', 'HIGH'),
)

STATUSES = (
    ('NEW', 'New Ticket'),
    ('PEN', 'Pending'),
    ('COM', 'Completed'),
)


class Unit(models.Model):
    unit_number = models.CharField(max_length=10)
    unit_status = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=False)
    
    def __str__(self):
        return self.unit_number
    
class Ticket(models.Model):
    category = models.CharField(
        max_length=3,
        choices=CATEGORIES,
    )
    priority = models.CharField(
        max_length=1,
        choices=PRIORITIES,
    )
    location = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    status =models.CharField(
        max_length=3,
        choices=STATUSES,
        default='NEW',
    )
    date_created = models.DateTimeField(default=datetime.now)
    completion_date = models.TimeField(null=True)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)

    def __str__(self):
        return self.description

    def get_absolute_url(self):
        return reverse('detail', kwargs={'ticket_id': self.id})

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    phone = models.CharField(max_length=13)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('index', kwargs={'profile_id': self.id})

class Photo(models.Model):
    url = models.CharField(max_length=200)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for ticket_id: {self.ticket_id} @{self.url}"