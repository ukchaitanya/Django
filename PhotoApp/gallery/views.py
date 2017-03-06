from django.shortcuts import render
from django.http import HttpResponse,Http404
from django.shortcuts import render
from .models import Album,Photo

def index(request):
	allAlbums = Album.objects.all()
	context = {	'all_albums': allAlbums }
	return render(request, 'html/index.html',context)

def details(request,albumId):
	try:
		album = Album.objects.get(id=albumId)
		allPhotos = Photo.objects.get(id=albumId)
	except Album.DoesNotExist:
		raise Http404("Album dos not exist")
	return render(request, 'html/details.html',{ 'album': album,'allPhotos':allPhotos })

	