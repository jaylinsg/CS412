# file hw/views.property

import random
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

import time

# Create your views here.
def home(request):
    '''fund to respond to the "home" request'''

    response_text = f'''
    <html>
    <h1>Hello World!</h1>
    The current time is {time.ctime()}.
    </html>
    '''
 
    return HttpResponse(response_text)

def home_page(request):
    '''Respond to the URL '', delegate work to a template.'''

    template_name = 'hw/home.html'
    context = {
        "time": time.ctime(),
        "letter1": chr(random.randint(65,90)),
        "letter2": chr(random.randint(65,90)),
        "number": random.randint(1,10),
    }

    return render(request, template_name, context)

def about(request):
    '''Define a view to show the 'about.html' template.'''

    # the template to which we will delegate the work
    template = 'hw/about.html'

    # a dict of key/value pairs, to be available for use in template
    context = {
        "time": time.ctime(),
        "letter1": chr(random.randint(65,90)),
        "letter2": chr(random.randint(65,90)),
        "number": random.randint(1,10),
    }

    return render(request, template, context)