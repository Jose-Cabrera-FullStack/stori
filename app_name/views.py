from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt

from app_name.serializer import RequestDataSerializer


# Option 1: Class based view
class AppNameAPIVIew(APIView):

    serializer_class = RequestDataSerializer

    def post(self, request, *args, **kwargs):

        return Response(data={"http_message": "SUCCESS", "data": "data"}, status=status.HTTP_200_OK)


# Option 2: Function based view
@csrf_exempt
@api_view(['POST'])
def post_endpoint(request):
    serializer = RequestDataSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(data={"http_message": "ERROR", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    return Response(data={"http_message": "SUCCESS", "data": "data"}, status=status.HTTP_200_OK)


@csrf_exempt
@api_view(['GET'])
def get_enpoint(request):
    serializer = RequestDataSerializer(data=request.data)

    return Response(data={"http_message": "SUCCESS", "data": "data"}, status=status.HTTP_200_OK)
