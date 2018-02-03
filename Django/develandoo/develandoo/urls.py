from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from myai import views as myai_views

urlpatterns = [
    path('', myai_views.home, name='home'),
    path('info/', myai_views.info, name='info'),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
