# alkaloid_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('peptaloids/', views.PeptaloidListCreate.as_view(), name='peptaloid-list-create'),
    path('peptaloids/<int:pk>/', views.PeptaloidDetail.as_view(), name='peptaloid-detail'),
]

