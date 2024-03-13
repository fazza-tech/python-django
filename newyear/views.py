from django.shortcuts import render

import datetime

# Create your views here.
def index(request): 
    #define now
    now = datetime.datetime.now()
    #return a template
    return render(request, "newyear/index.html", {
        #define the variable inside the template
        "newyear" : now.month ==1 and now.day ==1
    }) 