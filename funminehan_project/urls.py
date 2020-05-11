from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from main.sitemaps import StaticViewSitemap, OutreachSitemap, MemberSitemap

#REMEMBER TO REMOVE THIS SHIT WHILE GOING LIVE 
from django.conf import settings
from django.conf.urls.static import static



sitemaps = {
	"static": StaticViewSitemap,
	"outreach": OutreachSitemap,
	"member": MemberSitemap,

}

urlpatterns = [
	path('', include("main.urls")),

	path("sitemap.xml", sitemap, {"sitemaps": sitemaps}),
    path('admin/', admin.site.urls),
]



#REMEMBER TO REMOVE THIS SHIT WHILE GOING LIVE 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
