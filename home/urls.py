from django.urls import path
from . import views 


urlpatterns = [
    path('', views.index, name='index'),
    path('infinput', views.infinput, name='infinput'),
    path('display', views.display, name='display'),
    path('api/document-info/', views.document_info, name='document_info'),
    
]