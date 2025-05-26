from django.urls import path
from . import views

app_name = "event"

urlpatterns = [
    path("create/", views.CreateEvent.as_view(), name="create-event"),
    path("list/", views.EventListView.as_view(), name="event-list"),
    path("detail/<int:pk>/", views.EventDetailView.as_view(), name="event-detail"),
    path("mine-events/", views.MyEventListView.as_view(), name="my-event-list"),
    path("update/<int:pk>/", views.UpdateEventView.as_view(), name="update-event"),
    path("image/create/", views.EventImageCreateView.as_view(), name="create-event-image"),
    path("image/detail/<int:pk>/", views.EventImageDetailView.as_view(), name="event-image-detail"),
    path("image/list/", views.EventImageListView.as_view(), name="event-image-list"),
]
