from django.utils.cache import patch_cache_control

class CacheControlMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        patch_cache_control(response, public=True, max_age=2592000)
        return response
