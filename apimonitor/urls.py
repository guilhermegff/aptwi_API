
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import RedirectView


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url('^accounts/', include('django.contrib.auth.urls')),
    url(r'^', include('aptwi.urls')),
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
