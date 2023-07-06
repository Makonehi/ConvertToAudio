from django.urls import path
from . import views


urlpatterns = [
    path('home_board', views.test, name='board/home_board'),

]



