from django.contrib import admin
from un.models import Album, Photo

# Register your models here.
class PhotoAdmin(admin.ModelAdmin):
    fields = ['photo_user', 'photo_album', 'photo_name', 'photo_description','photo_date', 'photo_image']
    list_display= ( 'photo_album', 'photo_name','photo_date','photo_image', 'bit',)
    list_filter = ['photo_date']


admin.site.register(Album)
admin.site.register(Photo, PhotoAdmin)
