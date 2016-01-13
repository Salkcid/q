from django.http.response import HttpResponse, Http404
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response, redirect
from un.models import Album, Photo
from django.core.exceptions import ObjectDoesNotExist
from un.forms import PhotoForm
from django.core.context_processors import csrf
from django.contrib import auth


def albums(request):
#return HttpResponse("Hi, here are albums")
    return render_to_response('albums.html', {'albums': Album.objects.all(), 'username': auth.get_user(request).username})

#def album(request, album_id=1):
#    return render_to_response('album.html', {'albums': Album.objects.get(id=album_id), 'photos': Photo.objects.filter(photo_album_id=album_id)})

def album(request, album_id=1):
    photo_form = PhotoForm
    args = {}
    args.update(csrf(request))
    args['album'] = Album.objects.get(id=album_id)
    args['photos'] = Photo.objects.filter(photo_album_id=album_id)
    args['form'] = photo_form
    args['username'] = auth.get_user(request).username
    return render_to_response('album.html', args)

def addphoto(request, album_id):
    if request.POST:
        form = PhotoForm(request.POST)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.photo_album = Album.objects.get(id=album_id)
            photo.photo_user = request.user
            photo.photo_image = form.cleaned_data['photo_image']
            form.save()
    return redirect('/albums/get/%s/' % album_id)