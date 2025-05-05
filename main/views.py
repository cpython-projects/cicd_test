from django.shortcuts import render, redirect
from .models import Category, Reservation
from .forms import ReservationForm


def index(request):
    if request.method == 'POST':
        reservation_form = ReservationForm(request.POST)
        if reservation_form.is_valid():
            reservation_form.save(commit=True)
            return redirect('index')
    else:
        reservation_form = ReservationForm()




    categories = Category.objects.filter(is_visible=True)
    context = {
        'categories': categories,
        'reservation_form': reservation_form,
    }
    return render(request, 'main.html', context=context)