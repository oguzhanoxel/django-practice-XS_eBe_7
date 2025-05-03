from django.urls import path

from firstapp import views

urlpatterns = [
    path('reservation', views.home, name='home'),
    path('function', views.hello_world, name='function'),
    path('class', views.HelloView.as_view(), name='class'),
]