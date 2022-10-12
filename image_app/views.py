from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .serializers import ImageSerializer

def home(request):
    return HttpResponse("Home Route Calling...")

#https://www.django-rest-framework.org/api-guide/parsers/#fileuploadparser
class ImageUploadParser(FileUploadParser):
    media_type = 'image/*'

class ImageView(APIView):   
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated] 
    def post(self, request, format=None):        
        parser_class = (ImageUploadParser,)
        print('Dataaaaaa Print', request.data)
        image_serializer = ImageSerializer(data=request.data)        
        if image_serializer.is_valid():
            image_serializer.save()
            return Response(image_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(image_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        



