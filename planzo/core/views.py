from django.shortcuts import render
from .api_doc import user_endpoints, event_endpoints, event_image_endpoints


def index(request):
    return render(request, 'core/index.html', {
        "user_endpoints": user_endpoints,
        "event_endpoints": event_endpoints + event_image_endpoints
    })
