from django.urls import path
from . import views 
from library import settings 
from django.conf.urls.static import static 
# from library.settings import DEBUG, MEDIA_URL, MEDIA_ROOT, STATIC_URL, STATIC_ROOT



urlpatterns = [
    path('', views.index, name ='index'),
    path('upload/', views.upload_form, name="upload"),
    path('update/<int:book_id>', views.update, name='update' ),
    path('delete/<int:book_id>', views.delete, name='delete'),
    
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
#     urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
