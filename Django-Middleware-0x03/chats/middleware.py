from datetime import datetime, time, timedelta
from django.http import HttpResponseForbidden
from collections import defaultdict
import logging

logger = logging.getLogger(__name__)

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = request.user if request.user.is_authenticated else "Anonymous"
        logger.info(f"{datetime.now()} - User: {user} - path: {request.path}")
        return self.get_response(request)
    
class RestrictAccessByTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        current_time = datetime.now().time()

        start_time = time(00, 0)
        end_time = time(21, 0)

        if not (start_time <= current_time <= end_time):
            return HttpResponseForbidden(
"Access prohibited outside authorized hours (6 p.m. to 9 p.m.).")
        
        return self.get_response(request)
    
class OffensiveLanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.ip_message_log = defaultdict(list)
        self.message_limit = 5
        self.time_window = timedelta(minutes=1) 

    def __call__(self, request):
        if request.method == 'POST':
            ip_address = self.get_ip(request)
            now = datetime.now()

             # Cleaning up old queries
            self.ip_message_log[ip_address] = [
                ts for ts in self.ip_message_log[ip_address]
                if now - ts < self.time_window
            ]

            # Limit check
            if len(self.ip_message_log[ip_address]) >= self.message_limit:
                return HttpResponseForbidden("Too many messages sent. Wait a minute.")
            
            # Saving the new message
            self.ip_message_log[ip_address].append(now)

        return self.get_response(request)
     
    def get_ip(self, request):
        """Gets the client's IP address"""
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            return x_forwarded_for.split(',')[0]
        return request.META.get('REMOTE_ADDR')
    
class RolepermissionMiddleware:
    def __init__(self, get_response):
        self.get_response =  get_response

    def __call__(self, request):
        user =  request.user

        if user.is_authenticated:
            # Checks if the user's role is admin or moderator
            if not (user.is_superuser or getattr(user, 'role', '') in ['admin', 'moderator']):
                return HttpResponseForbidden("Access reserved for administrators or moderators.")
            
        else:
            # User is not logged in
            return HttpResponseForbidden("Authentication required.")
        
        return self.get_response(request)

