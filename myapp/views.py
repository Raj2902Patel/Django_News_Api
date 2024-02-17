from django.shortcuts import render
import requests

# Create your views here.


def index(request):
    records = {}
    url = "https://newsapi.org/v2/everything?q=india&from=2024-02-14&to=2024-02-14&sortBy=all&apiKey=25f76ba1c3584adfbd0539f9285beaf2"
    response = requests.get(url=url)
    appo_api = response.json()
    records['apidata'] = appo_api

    return render(request,'index.html',records)