from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from reader.models import Image, Comicbook
from reader.forms import ImageForm, ComicbookNameForm

# Create your views here.
# def index(request):
#     return  HttpResponse("Hello, world. you are in the reader index")


# def list(request):
#     # Handle file upload
#     if request.method == 'POST':
#         form = ImageForm(request.POST, request.FILES)
#         if form.is_valid():
#             newdoc = Image(imagefile = request.FILES['imagefile'])
#             newdoc.save()
#
#             # Redirect to the document list after POST
#             return HttpResponseRedirect(reverse('.views.list'))
#     else:
#         form = ImageForm() # A empty, unbound form
#
#     # Load documents for the list page
#     images = Image.objects.all()
#
#     # Render list page with the documents and the form
#     return render_to_response(
#         'lists.html',
#         {'images': images, 'form': form},
#         context_instance=RequestContext(request)
#     )
#
def base(request):
    return render_to_response('base.html')


def newcomic(request):
    # Handle file upload
    if request.method == 'POST':
        form = ComicbookNameForm(request.POST)
        if form.is_valid():
            newdoc = Comicbook(title = request.POST.get('title'), user=request.user)
            newdoc.save()
            print(newdoc)

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('reader-presentation', kwargs={'comic':newdoc.id}))
    else:
        form = ComicbookNameForm() # A empty, unbound form

    # Render list page with the documents and the form
    return render(request, 'comicbookname.html', {'form': form})

def upload(request):
    # Handle file upload
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            # newdoc = Image()
            form.save(commit=False)
            form.imagefile = request.FILES['imagefile']
            # form.save(commit=False)
            form.comicbook = Comicbook.objects.get(id=request.POST['comicbook'])
            form.name = request.POST['name']
            form.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect('/')
    else:
        form = ImageForm() # A empty, unbound form

    return render(request, 'uploadimage.html', {'form': form})


def presentation(request,comic):
    c = Comicbook.objects.get(id=comic)
    if request.method == 'POST':
        b = Image(comicbooktitle=request.POST['comicbook'], imagefile = request.FILES['imagefile'], name = request.POST['name'], user=request.user)

        b.save()
        c.pages.add(Image.objects.get(pk=b.pk))

        c.save()
    return render(request, 'cbrpresentation.html', {"cb": c})


def cbrview(request):
    images = Image.objects.all()
    return render(request, 'cbrview.html', {'images': images})
