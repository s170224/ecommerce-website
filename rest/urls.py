from django.urls import path
from .views import *


urlpatterns = [
    path('login/',user_login,name = 'login'),
    path('Home/', home, name='Home'),
    path('women/', women_data_view, name='women_data'),
    path('users/', user_data_view, name='user_data'),
    path('women_dresses/<str:id>/', women_items_data_view, name='women_dresses'),


]