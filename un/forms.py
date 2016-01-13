from django.forms import ModelForm
from un.models import Photo

class PhotoForm(ModelForm):
    class Meta():
        model = Photo
        fields = ['photo_name', 'photo_image', 'photo_description']
