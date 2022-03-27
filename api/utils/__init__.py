import json

from itertools import chain

from django.http import HttpRequest
from django.utils.translation import gettext_lazy as _
from rest_framework.request import Request

from proxies.utils import ProxyCommands


COMMANDS = [
    (command.value, command.label) for command in chain(ProxyCommands)
]

COMMAND_VALUES = [value for value, label in COMMANDS]


def is_jsonable(obj):
    try:
        json.dumps(obj)
        return True
    except (TypeError, OverflowError):
        return False


def parse_request_metadata(request, metadata={}):
    if metadata != {} and isinstance(metadata, dict):
        metadata = {
            key: value for key, value in metadata.items() if is_jsonable(value)
        }
    else:
        metadata = {}

    if isinstance(request, (Request, HttpRequest)):
        if hasattr(request, 'data') and isinstance(request.data, dict):
            metadata['request_data'] = {
                key: value for key, value in request.data.items() \
                if key not in ['password', 'password_2', 'current_password'] \
                and is_jsonable(value)
            }
        if hasattr(request, 'META') and isinstance(request.META, dict):
            for key, value in request.META.items():
                if is_jsonable(value):
                    metadata[key] = value
    elif isinstance(request, dict):
        for key, value in request.items():
            if is_jsonable(value):
                metadata[key] = value
    return metadata


__all__ = [
    'COMMANDS', 'COMMAND_VALUES', 'is_jsonable', 'parse_request_metadata',
]
