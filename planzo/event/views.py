from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView, ListAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import Event, EventImage
from .serializers import EventSerializer, EventImageSerializer

# Create your views here.



class CreateEvent(CreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]


# Third party Views
class EventListView(ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [AllowAny]

class EventDetailView(RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [AllowAny]


# My Event Views
class MyEventListView(ListAPIView):
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.request.user.hosted_events.all()

class UpdateEventView(UpdateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.request.user.hosted_events.all()

    def perform_update(self, serializer):
        serializer.save(host=self.request.user)


class EventImageCreateView(CreateAPIView):
    queryset = EventImage.objects.all()
    serializer_class = EventImageSerializer
    permission_classes = [IsAuthenticated]

class EventImageDetailView(RetrieveAPIView):
    queryset = EventImage.objects.all()
    serializer_class = EventImageSerializer
    permission_classes = [AllowAny]

class EventImageListView(ListAPIView):
    queryset = EventImage.objects.all()
    serializer_class = EventImageSerializer
    permission_classes = [AllowAny]
    def get_queryset(self):
        event_id = self.kwargs.get("event_id")
        return EventImage.objects.filter(event_id=event_id)

class UpdateEventImageView(UpdateAPIView):
    queryset = EventImage.objects.all()
    serializer_class = EventImageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        event_id = self.kwargs.get("event_id")
        return EventImage.objects.filter(event_id=event_id, event__host=self.request.user)

    def perform_update(self, serializer):
        event_id = self.kwargs.get("event_id")
        event = Event.objects.get(id=event_id, host=self.request.user)
        serializer.save(event=event)
