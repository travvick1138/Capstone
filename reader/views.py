from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from reader.models import Image, Comicbook
from reader.forms import ImageForm, ComicbookNameForm

# Create your views here.
# def index(request):
#     return  HttpResponse("Hello, world. you are in the reader index")


def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Image(imagefile = request.FILES['imagefile'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('.views.list'))
    else:
        form = ImageForm() # A empty, unbound form

    # Load documents for the list page
    images = Image.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'lists.html',
        {'images': images, 'form': form},
        # context_instance=RequestContext(request)
    )

def index(request):
    return render_to_response('index.html')


def newcomic(request):
    # Handle file upload
    if request.method == 'POST':
        form = ComicbookNameForm(request.POST)
        if form.is_valid():
            newdoc = Comicbook(title = request.POST['title'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('.views.upload'))
    else:
        form = ComicbookNameForm() # A empty, unbound form

    # Render list page with the documents and the form
    return render_to_response(
        'comicbookname.html',
        {'form': form},
        #RequestContext(request)
    )

def upload(request):
    return render_to_response('uploadimage.html')
