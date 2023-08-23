from django.urls import path
from stori.views import AppNameAPIVIew
from stori.views import post_endpoint, get_enpoint

stori = 'stori'

urlpatterns = [
    # Option 1: Class based view
    path("api/v1/stori/", AppNameAPIVIew.as_view(), name='stori'),

    # Option 2: Function based view
    path("api/v1/stori/", post_endpoint, name='post-endpoint-view'),
    path("api/v1/stori/", get_enpoint, name='get-enpoint-view'),
]
