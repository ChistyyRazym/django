from django.shortcuts import render
from django.http import HttpResponse
from .models import test_1
# Create your views here.

def index(request):
    print(request)
    log = test_1.objects.all()
    res = '<h1>---LogEntry---</h1>'
    for item in log:
        res += f'<table><td><p><b>ip</b>: {item.ip} </p></td>' \
               f'<td><p><b>date</b>: {item.date}</p></td>' \
               f'<td><p><b>method</b>: {item.method}</p></td>' \
               f'<td><p><b>url</b>: {item.url}</p></td>' \
               f'<td><p><b>status_code</b>: {item.status_code}</p></td>' \
               f'<td><p><b>response_size</b>: {item.response_size}</p></td></table>'
    return HttpResponse(res)