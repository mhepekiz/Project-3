from django.shortcuts import render, redirect
from .models import Unit, Ticket, Profile
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
@login_required
def home(request):
    return redirect('index')

@login_required
def tickets_index(request):
    user = request.user
    unit = Profile.objects.get(user=user)
    # user_unit = Unit.objects.filter(userid=users).values
    # tickets = Ticket.objects.filter(unit = .unit)
    tickets = Ticket.objects.filter(unit_id=unit)
    return render(request, 'tickets/index.html', {'users': user, 'unit': unit, 'tickets': tickets })

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)
