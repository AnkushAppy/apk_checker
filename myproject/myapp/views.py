# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from myproject.myapp.models import Document
from myproject.myapp.models import FileInfo
from myproject.myapp.forms import DocumentForm
from androguard.core.bytecodes import apk
#import xml.etree.ElementTree as ET
from myproject.myapp.task import apk_reader 

"""
from androguard.core.bytecodes import apk
a=apk.APK('/Users/dolcera23/Desktop/sample_apk/com.olacabs.customer.3.4.09.apk')
d = a.get_AndroidManifest()
d.toxml() --> xml 

"""


def list(request):
    # Handle file upload
    
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'])
            newdoc.save()
            apk_reader.delay(newdoc.docfile.url, request.FILES['docfile'].name)

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('myproject.myapp.views.list'))
    else:
        form = DocumentForm()  # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()
    fileinfos = FileInfo.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'list2.html',
        {'documents': documents, 'form': form, 'fileinfos':fileinfos },
        context_instance=RequestContext(request))


    


def list3(request):
    documents = Document.objects.all()
    fileinfos = FileInfo.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'list3.html',
        {'documents': documents, 'fileinfos':fileinfos },
        context_instance=RequestContext(request))



