from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .models import Reminder
from .serializers import Reminderserializer

# Create your views here.
@api_view(['GET'])
def home(request):
    object = Reminder.objects.all()
    serializer = Reminderserializer(object, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def remind_me(request):
    date = request.data.get('date')
    message = request.data.get('message')
    Reminder.objects.create(date=date, message=message)
    return Response({'message': 'Created successfully !!'}, status=status.HTTP_200_OK)