from django.urls import path
from stori.views import summary_balance

stori = 'stori'

urlpatterns = [
    path("api/v1/summary_balance/", summary_balance, name='summary_balance'),
]
