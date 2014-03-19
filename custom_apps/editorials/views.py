
from django.http import HttpResponse #, HttpResponseRedirect, Http404
from django.template import RequestContext, Context
from django.shortcuts import render_to_response, get_object_or_404

from models import Editorial


try:

    current_editorials[0]
except: 
    current_editorials = Editorial.objects.all()

def editorial_random(request):
    context = {}
    context['editorial'] = current_editorials

    template = 'base.html'
    return render_to_response(template, context_instance=RequestContext(request, context))


def editorial_list(request):
    context = {}

    try:
        context['editorial_list'] = current_editorials
        context['current_exhibits'] = True
    except:
        context['editorial_list'] = Editorial.objects.all()
        context['current_exhibits'] = False
        

    template = 'editorials/list.html'
    return render_to_response(template, context_instance=RequestContext(request, context))


def editorial_detail(request, pk):
    context = {}
    e = Editorial.objects.get(pk=pk)
    context['editorial'] = e
    context['editorial_list'] = Editorial.objects
    
    template = 'editorials/detail.html'
    return render_to_response(template, context_instance=RequestContext(request, context))


def editorial_archive(request):
    context = {}
    context['archive'] = True
    context['editorial_list'] = Editorial.objects
    template = 'editorials/list.html'
    return render_to_response(template, context_instance=RequestContext(request, context))



    
