from django.urls import path
from near import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('save_coordinates_in_db_and_file', views.save_coordinates_in_db_and_file, name="save_coordinates_in_db_and_file"),
]

# if settings.DEBUG:
#     urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    