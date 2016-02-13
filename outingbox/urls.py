from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^$', views.index_view, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^get_nearby/$', views.get_nearby, name='get_nearby'),
    url(r'^contact$', views.contact_us_view, name='contact'),
    url(r'^about$', views.about_us_view, name='about'),
    url(r'^search/$', views.search_view, name='search'),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^accounts/profile/$', views.profile_view, name='profile'),
    url(r'^accounts/profile/bookmarks$', views.profile_bookmarks_view, name='profile_bookmarks'),
    url(r'^accounts/bookmark/$', views.bookmark_activity, name='bookmark'),
    url(r'^accounts/rate/$', views.rate_activity, name='rate'),
    url(r'^accounts/comment/$', views.comment_activity, name='comment'),
    url(r'^activity/(?P<id>[\w, -]+)/(?P<title>[\w, -]+)/$', views.activity_view, name='activity'),
    url(r'^box/(?P<id>[\w, -]+)/(?P<title>[\w, -]+)/$', views.box_view, name='box'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
