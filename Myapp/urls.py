
from django.urls import path
from . import views
# from .views import chat_view, schedule_appointment

urlpatterns = [
    path('', views.index_pro, name='index_pro'),
    path('login_page/',views.login_page,name='login_page'),
    path('register/',views.register,name='register'),
    path('index_page/',views.index_page,name='index_page'),
  
]
