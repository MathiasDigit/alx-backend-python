from datetime import datetime, time
from django.http import HttpResponseForbidden
import logging

logger = logging.getLogger(__name__)

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = request.user if request.user.is_authenticated else "Anonymous"
        logger.info(f"{datetime.now()} - User: {user} - path: {request.path}")
        return self.get_response(request)
    
class RestrictAccesByTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        current_time = datetime.now().time()

        start_time = time(18, 0)
        end_time = time(21, 0)

        if not (start_time <= current_time <= end_time):
            return HttpResponseForbidden(
"Access prohibited outside authorized hours (6 p.m. to 9 p.m.).")
        
        return self.get_response(request)