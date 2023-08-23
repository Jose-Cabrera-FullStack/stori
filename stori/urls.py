from django.urls import path
from stori.views import user_balance

stori = 'stori'

urlpatterns = [
    path("api/v1/user_balance/", user_balance, name='user_balance'),
]
