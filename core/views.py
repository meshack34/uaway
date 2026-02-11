from django.shortcuts import render

# ---------- Public ----------
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegisterForm
from django.shortcuts import render


def home_view(request):
    return render(request, "home.html")

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = RegisterForm()

    return render(request, 'home/register.html', {'form': form})

from django.contrib.auth.decorators import login_required
from .decorators import role_required
# from .models import Trip


# @login_required
# @role_required(['driver', 'both'])
# def create_trip(request):
#     if request.method == 'POST':
#         Trip.objects.create(
#             driver=request.user,
#             origin=request.POST['origin'],
#             destination=request.POST['destination'],
#             departure_date=request.POST['departure_date'],
#             departure_time=request.POST['departure_time'],
#             total_seats=request.POST['total_seats'],
#             available_seats=request.POST['total_seats'],
#             price_per_seat=request.POST['price_per_seat'],
#             notes=request.POST.get('notes', '')
#         )
#         return redirect('dashboard')

#     return render(request, 'create_trip.html')



@login_required
def dashboard(request):
    if request.user.role in ['driver', 'both']:
        return render(request, 'driver_dashboard.html')
    return render(request, 'passenger_dashboard.html')
