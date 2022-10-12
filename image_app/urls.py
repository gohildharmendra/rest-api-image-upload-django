from django.urls import path, include
from image_app import views
app_name='image_app'

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('',views.home, name='home'),
    path('upload/',views.ImageView.as_view()),    
    #Generate AuthToken
    path('gettoken/', obtain_auth_token),
]