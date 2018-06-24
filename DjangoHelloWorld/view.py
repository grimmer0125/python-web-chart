# added by grimmer, hello world example
from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello world ! ")

# template render example:
# https://github.com/twtrubiks/django-tutorial/blob/master/musics/views.py
#     return render(request, 'hello_django.html', {
#         'data': "Hello Django ",
#         'musics': musics,
#     })
