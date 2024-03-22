from django.shortcuts import render
from django.http import HttpResponse
from photos.models import photo, page


def index(request):
    
    img_list = photo.objects.order_by('imagename')
    context_dict = {'images': img_list}
    
    return render(request, 'photos/photos.html', context= context_dict)

# Create your views here.
