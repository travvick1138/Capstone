# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.template import RequestContext
from django.contrib.auth.models import User
from django.http import JsonResponse,HttpResponse,HttpResponseRedirect
from django.utils import timezone
from django.core.urlresolvers import reverse
from .models import Comicbook
from .forms import ComicbookForm
import datetime

# Create your views here.

def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['comicfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('.views.list'))
    else:
        form = ComicbookForm() # A empty, unbound form

    # Load documents for the list page
    comicbooks = Comicbook.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'templates/list.html',
        {'documents': documents, 'form': form},
        context_instance=RequestContext(request)
    )
# From https://github.com/giacomos/collective.comicbookreader updated https://github.com/travvick1138
