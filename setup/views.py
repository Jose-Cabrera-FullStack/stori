from django.http.response import HttpResponse
from rest_framework.decorators import api_view


def greeting(request):
    return HttpResponse({"http_message": "SUCCESS",
                         "data": "django base project"})
