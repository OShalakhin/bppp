#-*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext


def home_page(request):
    """home page"""
    return render_to_response(
        'home.html',
        context_instance=RequestContext(request))
