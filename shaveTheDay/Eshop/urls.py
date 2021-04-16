from django.contrib import admin
from django.urls import path  , include
from django.conf.urls.static import static
from . import settings
from django.contrib.auth import views as auth_views
admin.site.site_header = 'Shave The Day Inc.'
admin.site.site_title = 'Shave the Day Inc. Admin'
admin.site.index_title = 'ShaveTheDay Administration'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , include('store.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
