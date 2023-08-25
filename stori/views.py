from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt

from stori.services import StoriService
from stori.serializer import RequestDataSerializer


@csrf_exempt
@api_view(['GET'])
def summary_balance(request):
    # serializer = RequestDataSerializer(data=request.data)
    data = StoriService.send_summary_balance(request)
    return Response(data={"http_message": "SUCCESS", "data": data}, status=status.HTTP_200_OK)
