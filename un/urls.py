from django.conf.urls import include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # Examples:
    # url(r'^$', 'firstapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^albums/all/$', 'un.views.albums'),
    url(r'^albums/get/(?P<album_id>\d+)/$', 'un.views.album'),
    url(r'^album/addphoto/(?P<album_id>\d+)/$', 'un.views.addphoto'),
    url(r'^auth/', include('loginsys.urls')),
    url(r'^$', 'un.views.albums')
#url(r'^articles/all/$', 'article.views.articles'),
#url(r'^articles/get/(?P<article_id>\d+)/$', 'article.views.article'),
#url(r'^', 'article.views.articles'),
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns() + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


