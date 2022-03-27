import logging

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from rest_framework.exceptions import Throttled
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from proxies.get_proxies import get_proxies
from proxies.permissions import ReadOnly
from proxies.utils import ProxyCommands

from utils import parse_request_metadata
from utils.exceptions import RequestError
from utils.throttling import throttle_command


logger = logging.getLogger(__name__)

class ProxiesAPI(APIView):
    permission_classes = (ReadOnly,)
    renderer_classes = (JSONRenderer,)

    @method_decorator(cache_page(600))
    def get(self, request: Request, *args, **kwargs):
        try:
            if throttle_command(
                ProxyCommands.GET_PROXIES, request.META['CLIENT_IP'], request,
            ):
                raise Throttled()
            proxies = get_proxies()
        except Throttled as e:
            raise e
        except Exception as e:
            logger.exception('Error getting proxies.', exc_info=e, extra={
                'command': ProxyCommands.GET_PROXIES,
                'client_ip': request.META['CLIENT_IP'],
                'metadata': parse_request_metadata(request),
            })
            raise RequestError('Error retrieving proxies.')
        return Response(data=proxies, content_type='application/json')
