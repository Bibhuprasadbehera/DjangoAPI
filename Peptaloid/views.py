#views.py

from django.http import HttpResponse
from rest_framework import generics
from .models import Peptaloid
from .serializers import PeptaloidSerializer

class PeptaloidListCreate(generics.ListCreateAPIView):
    queryset = Peptaloid.objects.all()
    serializer_class = PeptaloidSerializer

class PeptaloidDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Peptaloid.objects.all()
    serializer_class = PeptaloidSerializer
    
def home(request):
    return HttpResponse("Hello, World!")

