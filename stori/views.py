from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt

from stori.serializer import RequestDataSerializer


@csrf_exempt
@api_view(['GET'])
def user_balance(request):
    serializer = RequestDataSerializer(data=request.data)

    return Response(data={"http_message": "SUCCESS", "data": "data"}, status=status.HTTP_200_OK)
