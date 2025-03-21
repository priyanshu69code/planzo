from rest_framework import serializers
from django.contrib.auth import authenticate
from django.utils import timezone
from .models import Event, EventImage
from user.serializers import UserSerializer
from user.models import MyUser


class EventImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventImage
        fields = "__all__"

    def create(self, validated_data):
        event = validated_data["event"]
        if event.host != self.context["request"].user:
            raise serializers.ValidationError("You are not the host of this event.")
        image = EventImage.objects.create(**validated_data)
        return image


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ["id", "name", "description", "start_date", "end_date", "time", "location", "created_at", "updated_at", "host", "venue", "capacity", "attendees", "is_free", "price", "is_online"]
        read_only_fields = ["created_at", "updated_at", "host", "attendees"]

    def create(self, validated_data):
        user = self.context["request"].user
        event = Event.objects.create(host=user, **validated_data)
        return event
