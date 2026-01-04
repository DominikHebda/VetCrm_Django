from django.shortcuts import render

from .models import Appointment


# Create your views here.
def appointment_list(request):
    appointments = Appointment.objects.select_related('pet', 'doctor')
    return render(
        request,
        'core/appointment_list.html',
        {'appointments': appointments}
    )