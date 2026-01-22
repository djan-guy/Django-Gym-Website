from django.urls import path
from . import views

app_name = 'membership'

urlpatterns = [
    path('', views.membership_page, name='membership_page'),
    path('verification/', views.membership_verification, name='membership_verification'),
]
