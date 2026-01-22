from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = "page"

urlpatterns = [
    path('', views.page_list, name="list"),
    path('page-new/', views.page_new, name="page-new"),
    path('<int:pk>/delete/', views.page_delete, name='page-delete'),
    path('<slug:slug>', views.page_list, name="page"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
