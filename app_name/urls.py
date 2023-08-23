from django.urls import path
from app_name.views import AppNameAPIVIew
from app_name.views import post_endpoint, get_enpoint

app_name = 'app_name'

urlpatterns = [
    # Option 1: Class based view
    path("api/v1/app_name/", AppNameAPIVIew.as_view(), name='app_name'),

    # Option 2: Function based view
    path("api/v1/app_name/", post_endpoint, name='post-endpoint-view'),
    path("api/v1/app_name/", get_enpoint, name='get-enpoint-view'),
]
