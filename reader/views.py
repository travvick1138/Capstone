from django import forms
from django.utils.text import slugify
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from reader.models import Image, Comicbook
from reader.forms import ImageForm, ComicbookNameForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/accounts/login/")
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {
        'form': form,
    })


@login_required
def profile(request):
    user = request.user
    comicbooklist = Comicbook.objects.filter(user=request.user)

    return render(request, "profile.html", {'comicbooklist': comicbooklist})

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
# def base(request):
#     return render_to_response('base.html')


def newcomic(request):
    # Handle file upload
    if request.method == 'POST':
        form = ComicbookNameForm(request.POST)
        if form.is_valid():
            newdoc = Comicbook(title = request.POST.get('title'), user=request.user, slug=slugify(request.POST.get('title')))
            newdoc.save()
            print(newdoc)

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('reader-presentation', kwargs={'comic':newdoc.slug}))
    else:
        form = ComicbookNameForm() # A empty, unbound form

    # Render list page with the documents and the form
    return render(request, 'comicbookname.html', {'form': form})


def presentation(request,slug):
    c = Comicbook.objects.get(slug=slug)
    if request.method == 'POST':
        b = Image(comicbooktitle=request.POST['comicbook'], imagefile = request.FILES['imagefile'], name = request.POST['name'], user=request.user)

        b.save()
        c.pages.add(Image.objects.get(pk=b.pk))

        c.save()
    return render(request, 'cbrpresentation.html', {"cb": c})


def cbrview(request,slug):
    comicbook = Comicbook.objects.get(slug=slug)
    return render(request, 'cbrview.html', {'comicbook': comicbook})


def instructions(request):
    return render(request, 'instructions.html')
