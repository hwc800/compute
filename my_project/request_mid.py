
import time
from django.utils import timezone

from auto.models import RequestTime


class RequestTimingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = timezone.now()
        request.start_time = start_time
        response = self.get_response(request)
        end_time = timezone.now()
        duration = end_time - start_time

        RequestTime.objects.create(
            path=request.path,
            start_time=start_time,
            end_time=end_time,
            status_code=response.status_code,
        )
        return response