from django.urls import path
from profiles.views import view

app_name = 'profile'

urlpatterns = [
    path('', profile_view, name='profile'),
]
