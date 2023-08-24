from django.utils.cache import patch_cache_control

class CacheControlMiddleware:
    """
    Middleware to add cache control headers to HTTP responses.

    This middleware adds cache control headers to the HTTP responses
    based on the specified parameters. It sets the response as public
    and sets a maximum age for caching.

    Attributes:
        get_response (callable): The callable that represents the next
            middleware or view in the chain.
    """

    def __init__(self, get_response):
        """
        Initialize the CacheControlMiddleware.

        Args:
            get_response (callable): The callable that represents the next
                middleware or view in the chain.
        """
        self.get_response = get_response

    def __call__(self, request):
        """
        Process the request and response.

        This method is called for each incoming request. It processes
        the request using the specified middleware or view and then
        adds cache control headers to the response.

        Args:
            request (HttpRequest): The incoming HTTP request.

        Returns:
            HttpResponse: The processed HTTP response with cache control headers.
        """
        response = self.get_response(request)
        patch_cache_control(response, public=True, max_age=259200)
        return response