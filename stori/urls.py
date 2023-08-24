from django.urls import path
from stori.views import summary_balance

stori = 'stori'

urlpatterns = [
    path("api/v1/user_balance/", summary_balance, name='user_balance'),
]
