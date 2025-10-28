import sqlite3
from django.http import JsonResponse

class IgnoreSQLiteLockMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            return self.get_response(request)
        except sqlite3.OperationalError as e:
            if "database is locked" in str(e):
                # You can return  a simple 503, or an empty response
                return JsonResponse({"status": "ignored_due_to_lock"}, status=503)
            raise