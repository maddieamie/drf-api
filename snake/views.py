from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Snake
from .serializers import SnakeSerializer

class SnakeList(ListCreateAPIView):
    # Anything that inherits from ListAPI View is going to need 2 things.
    # What is the collection of things, aka the queryset
    queryset = Snake.objects.all()

    #serializing
    serializer_class = SnakeSerializer

# The ThingDetail needs the same things
class SnakeDetail(RetrieveUpdateDestroyAPIView):
    queryset = Snake.objects.all()
    serializer_class = SnakeSerializer
