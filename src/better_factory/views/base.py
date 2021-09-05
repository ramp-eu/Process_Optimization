from pyramid.view import view_defaults
from sqlalchemy.orm import Session, joinedload
from tet.view import ServiceViews
from tet.services import autowired

from .. import models
from .exceptions import ApiError


@view_defaults(
    renderer='json',
)
class BaseApi(ServiceViews):
    # db_session = autowired(Session)

    # default_validators = ['validate_auth_token']
    default_validators = []
    validators = []

    def __init__(self, request, context=None):
        super().__init__(request)

        self._validate_request(request)

    def _validate_request(self, request):
        validators = self.default_validators + self.validators
        for validator in validators:
            getattr(self, validator)(request)

    def validate_auth_token(self, request):
        # NOTE: pyramid_jwt takes care of validating the token, including
        # checking the expiration time
        if not request.authenticated_userid:
            raise ApiError('Invalid authentication token', status=401)
