from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from DataWranglingApp.models import Airlines, Flights

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def airlines(request):
    template = loader.get_template('airlines.html')

    airlines = Airlines.objects.all()

    context = {
        'objects': airlines
    }

    return HttpResponse(template.render(context))

def top(request):
    template = loader.get_template('top.html')

    top_dest = Flights.objects.raw("SELECT 1 id, a.name AS dest, COUNT(*) AS total FROM `Flights` f INNER JOIN `Airports` a ON f.dest = a.faa GROUP BY dest ORDER BY COUNT(*) DESC")[:10]
    top_origin = Flights.objects.raw("SELECT 1 id, a.name AS ogn, COUNT(*) AS total FROM `Flights` f INNER JOIN `Airports` a ON f.origin = a.faa GROUP BY origin ORDER BY COUNT(*) DESC")[:10]

    context = {
        'top_dest': top_dest,
        'top_origin': top_origin
    }

    return HttpResponse(template.render(context))


