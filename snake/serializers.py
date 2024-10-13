from rest_framework import serializers
from .models import Snake

class SnakeSerializer(serializers.ModelSerializer):
  class Meta:
    fields = ("id","owner","name","description","color","breed","created_at")
    model = Snake




