from django.shortcuts import render, redirect, get_object_or_404,render_to_response,RequestContext
from django.forms import ModelForm
from django.http import HttpResponse
from django.contrib import auth
from django.core.context_processors import csrf
from django.core.context_processors import request
from django.core.context_processors import request
from django.http import HttpResponse
from httplib import HTTPResponse
from django.template import Context,loader

def index(request):
    return  render_to_response("pages/calendar.html",locals(),context_instance=RequestContext(request))
