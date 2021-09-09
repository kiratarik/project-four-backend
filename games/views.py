from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Game
from .serializers import GameSerializer

# Create your views here.
class GameListView(ListCreateAPIView):
    '''List View for /games INDEX CREATE'''
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = ( IsAuthenticatedOrReadOnly, )
