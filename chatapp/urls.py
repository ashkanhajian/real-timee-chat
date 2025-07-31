from . import views
from django.urls import path
app_name = 'chatapp'
urlpatterns = [
    path('', views.index, name= "index"),
    path('friends/<str:pk>', views.detail, name='detail'),
]