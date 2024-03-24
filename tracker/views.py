from django.shortcuts import render

# Create your views here.
# tracker/views.py

from django.shortcuts import render
from django.http import HttpResponse


def reduce_intake_view(request):
    # Your view logic here
    return render(request, 'tracker/reduce_intake.html')
