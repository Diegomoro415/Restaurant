from django.test import TestCase, RequestFactory
from django.http import HttpResponse
from django.utils.cache import patch_cache_control

class CacheControlMiddlewareTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_cache_control_middleware(self):
        """
        Test the CacheControlMiddleware by simulating a request and checking the cache control headers.
        """
        def mock_get_response(request):
            response = HttpResponse()
            patch_cache_control(response, public=True, max_age=259200)
            return response

        middleware = CacheControlMiddleware(mock_get_response)
        request = self.factory.get('/')
        response = middleware(request)

        self.assertEqual(response['Cache-Control'], 'public, max-age=259200')

# Middleware class
class CacheControlMiddleware:
    """
    Middleware to set Cache-Control headers on responses.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        """
        Add Cache-Control headers to the response.
        """
        response = self.get_response(request)
        patch_cache_control(response, public=True, max_age=259200)
        return response
