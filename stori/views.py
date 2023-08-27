from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt

from stori.services import StoriService
from stori.serializer import RequestDataSerializer


@csrf_exempt
@api_view(['POST'])
def summary_balance(request):
    serializer = RequestDataSerializer(data=request.data)
    if serializer.is_valid():
        summary_balance = StoriService.send_summary_balance(
            serializer.validated_data['email_recipient']
        )
    else:
        return Response(data={"http_message": "ERROR", "summary_balance": "Invalid email address. Please provide a valid email address."}, status=status.HTTP_400_BAD_REQUEST)

    return Response(data={"http_message": "SUCCESS", "summary_balance": summary_balance}, status=status.HTTP_200_OK)
