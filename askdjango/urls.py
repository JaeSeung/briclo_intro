from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import redirect
from home import views
urlpatterns = [
    url(r'^$', views.intro, name="intro"),
    url(r'^admin/', admin.site.urls),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^$', lambda request: redirect('blog:index')),
]

urlpatterns += static(settings.MEDIA_URL,
   document_root=settings.MEDIA_ROOT)