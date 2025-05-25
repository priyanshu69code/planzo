user_endpoints = [
    {
        "name": "Register User",
        "url": "/planzo/v1/user/register/",
        "method": "POST",
        "auth": "None",
        "request": {
            "email": "string (required, valid email)",
            "password": "string (required, min 6 characters)"
        },
        "response": {
            "email": "string"
        }
    },
    {
        "name": "Login",
        "url": "/planzo/v1/user/login/",
        "method": "POST",
        "auth": "None",
        "request": {
            "email": "string (required)",
            "password": "string (required)"
        },
        "response": {
            "refresh": "string (JWT refresh token)",
            "access": "string (JWT access token)",
            "user": {
                "id": "integer",
                "email": "string",
                "date_of_birth": "YYYY-MM-DD or null",
                "is_active": "boolean",
                "is_admin": "boolean"
            }
        }
    },
    {
        "name": "Get User Details",
        "url": "/planzo/v1/user/me/",
        "method": "GET",
        "auth": "Required (IsAuthenticated, IsVerified)",
        "request": {},
        "response": {
            "id": "integer",
            "email": "string",
            "date_of_birth": "YYYY-MM-DD or null",
            "is_active": "boolean",
            "is_admin": "boolean"
        }
    },
    {
        "name": "Update User",
        "url": "/planzo/v1/user/update/",
        "method": "PUT / PATCH",
        "auth": "Required (IsAuthenticated, IsVerified)",
        "request": {
            "email": "string (optional)",
            "date_of_birth": "YYYY-MM-DD (optional)"
        },
        "response": {
            "email": "string",
            "date_of_birth": "YYYY-MM-DD or null"
        }
    },
    {
        "name": "Refresh Token",
        "url": "/planzo/v1/user/token/refresh/",
        "method": "POST",
        "auth": "None",
        "request": {
            "refresh": "string (JWT refresh token)"
        },
        "response": {
            "access": "string (new JWT access token)"
        }
    }
]

event_endpoints = [
    {
        "name": "Create Event",
        "url": "/planzo/v1/event/create/",
        "method": "POST",
        "auth": "Required (IsAuthenticated)",
        "request": {
            "name": "string (max 100)",
            "description": "string",
            "start_date": "YYYY-MM-DD",
            "end_date": "YYYY-MM-DD",
            "time": "HH:MM:SS",
            "location": "string (max 100)",
            "venue": "string (max 100)",
            "capacity": "integer",
            "is_free": "boolean (optional)",
            "price": "decimal (optional)",
            "is_online": "boolean (optional)"
        },
        "response": {
            "id": "integer",
            "name": "string",
            "host": "user ID",
            "created_at": "datetime",
            "updated_at": "datetime"
        }
    },
    {
        "name": "List Events",
        "url": "/planzo/v1/event/list/",
        "method": "GET",
        "auth": "None",
        "request": {},
        "response": "Array of Event Objects"
    },
    {
        "name": "Get Event Details",
        "url": "/planzo/v1/event/detail/<int:pk>/",
        "method": "GET",
        "auth": "None",
        "request": {
            "pk": "integer (Event ID)"
        },
        "response": "Event Object"
    },
    {
        "name": "List My Events",
        "url": "/planzo/v1/event/my-events/",
        "method": "GET",
        "auth": "Required (IsAuthenticated)",
        "request": {},
        "response": "Array of Event Objects"
    },
    {
        "name": "Update Event",
        "url": "/planzo/v1/event/update/<int:pk>/",
        "method": "PUT / PATCH",
        "auth": "Required (IsAuthenticated)",
        "request": {
            "pk": "integer (Event ID)",
            "name": "string (optional)",
            "description": "string (optional)",
            "start_date": "YYYY-MM-DD (optional)",
            "end_date": "YYYY-MM-DD (optional)",
            "time": "HH:MM:SS (optional)",
            "location": "string (optional)",
            "venue": "string (optional)",
            "capacity": "integer (optional)",
            "is_free": "boolean (optional)",
            "price": "decimal (optional)",
            "is_online": "boolean (optional)"
        },
        "response": "Updated Event Object"
    }
]

event_image_endpoints = [
    {
        "name": "Create Event Image",
        "url": "/planzo/v1/event/image/create/",
        "method": "POST",
        "auth": "Required (IsAuthenticated)",
        "request": {
            "event": "integer (Event ID)",
            "image": "file (image)",
            "is_thumbnail": "boolean (optional)"
        },
        "response": {
            "id": "integer",
            "event": "integer",
            "image": "URL",
            "is_thumbnail": "boolean"
        }
    },
    {
        "name": "Get Event Image Details",
        "url": "/planzo/v1/event/image/detail/<int:pk>/",
        "method": "GET",
        "auth": "None",
        "request": {
            "pk": "integer (Image ID)"
        },
        "response": "Image Object"
    },
    {
        "name": "List Event Images",
        "url": "/planzo/v1/event/image/list/?event_id=<int>",
        "method": "GET",
        "auth": "None",
        "request": {
            "event_id": "integer (Event ID)"
        },
        "response": "Array of Image Objects"
    }
]
