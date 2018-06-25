# added by grimmer, hello world example
from django.http import HttpResponse

from datetime import datetime
from django.shortcuts import render

# def hello(request):
#     return HttpResponse("Hello world ! ")

# template render example:
# https://github.com/twtrubiks/django-tutorial/blob/master/musics/views.py
#     return render(request, 'hello_django.html', {
#         'data': "Hello Django ",
#         'musics': musics,
#     })

# TODO: 1. embed plotly charts in html
# 2. embed customized menu items <- using react possible?
#

def hello(request):
    return render(request, 'hello_world.html', {
        'current_time': str(datetime.now()),
    })
