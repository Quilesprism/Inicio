from . import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static 

app_name="CV"

urlpatterns= [
    path('', views.upload_file, name="home"), 
]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)