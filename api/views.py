from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# end points

def main(resquest):
    return HttpResponse("Hello Javier")
    