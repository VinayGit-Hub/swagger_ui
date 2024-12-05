from rest_framework.viewsets import ModelViewSet
from .models import Stream
from .serializers import StreamSerializer

class StreamViewSet(ModelViewSet):
    queryset = Stream.objects.all()
    serializer_class = StreamSerializer
