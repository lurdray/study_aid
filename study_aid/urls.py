from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from main.sitemaps import StaticViewSitemap, StudyResourceSitemap
from django.conf import settings
from django.conf.urls.static import static


sitemaps = {
	"static": StaticViewSitemap,
	"study_resource": StudyResourceSitemap,

}


urlpatterns = [
    path('admin/', admin.site.urls),

    path("", include("app_user.urls")),
    path("", include("cbt.urls")),
    path("", include("compete.urls")),
    path("", include("main.urls")),
    path("", include("question.urls")),
    path("", include("study_resource.urls")),
    path("", include("theory.urls")),

	path("sitemap.xml", sitemap, {"sitemaps": sitemaps}),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)