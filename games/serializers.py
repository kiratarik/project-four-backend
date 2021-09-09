from django.contrib.auth import get_user_model
from rest_framework import serializers

# from jwt_auth.serializers import UserProfileSerializer
from .models import Game
User = get_user_model()

class GameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Game
        fields = '__all__'