from django.db import models
from django.utils import timezone
from django.urls import reverse

class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    host = models.ForeignKey("user.MyUser", on_delete=models.CASCADE, related_name="hosted_events")
    venue = models.CharField(max_length=100)
    capacity = models.PositiveIntegerField()
    attendees = models.ManyToManyField("user.MyUser", related_name="events_attending", blank=True)
    is_free = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null
=True)
    is_online = models.BooleanField(default=False)


    def __str__(self):
        return self.name

    def is_multi_day(self):
        """Check if the event spans multiple days."""
        return self.start_date != self.end_date

    def is_upcoming(self):

        return self.start_date > timezone.now().date()

    def is_past(self):
        return self.end_date < timezone.now().date()

    def is_today(self):
        return self.start_date == timezone.now().date()

    def check_if_free(self):
        return self.is_free

    def attendess_count(self):
        return self.attendees.count()

    def free_capacity(self):
        if self.capacity == 0:
            return 0
        return self.capacity - self.attendees.count()  # Return the value instead of modifying capacity

    def get_absolute_url(self):
        return reverse('event:event-detail', kwargs={'pk': self.pk})



class EventImage(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="event_images")
    is_thumbnail = models.BooleanField(default=False)

    def __str__(self):
        return f"Image for {self.event.name}"
