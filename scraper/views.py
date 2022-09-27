from django.shortcuts import render
from django.http import HttpResponse


def scrape(request):
    return render(request, 'scraper/scrape.html')

