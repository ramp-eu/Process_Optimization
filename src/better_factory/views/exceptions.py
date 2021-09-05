from pyramid.view import exception_view_config
from pyramid import exceptions
from marshmallow import ValidationError


class ApiError(Exception):
    def __init__(self, message, *, status=400):
        self.message = message
        self.status = status


@exception_view_config(ApiError, renderer='json')
def api_error_view(exc, request):
    request.response.status = exc.status
    return {'error': exc.message}


@exception_view_config(ValidationError, renderer='json')
def validation_error_view(exc, request):
    request.response.status = 400
    return {'error': exc.messages}


@exception_view_config(exceptions.PredicateMismatch, renderer='json')
def predicate_mismatch_error_view(exc, request):
    if 'request_method =' in exc.message:
        request.response.status = 405
    return {'error': str(exc)}
