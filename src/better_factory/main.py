import sys

import sentry_sdk
from sentry_sdk.integrations.pyramid import PyramidIntegration
from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.security import ALL_PERMISSIONS, Allow
from tet.config import application_factory


class RootACL():
    __acl__ = [
        # (Allow, 'group:api', [
        #     'input_data:read',
        #     'input_data:create',
        # ]),
    ]

    def __init__(self, request):
        pass


def resolve_principals(userid, request):
    return [f'group:{r}' for r in request.jwt_claims.get('roles', [])]


@application_factory(excluded_features=(
    'renderers.tonnikala',
    'renderers.tonnikala.i18n',
))
def main(config):
    if sys.version_info < (3, 7):
        raise RuntimeError('This app needs python 3.7+')

    settings = config.get_settings()

    # external
    if settings.get('sentry.dsn'):
        sentry_sdk.init(
            dsn=settings['sentry.dsn'],
            integrations=[PyramidIntegration()],
            environment=settings['sentry.environment'],
        )

    config.include('pyramid_tm')
    # config.include('pyramid_jwt')

    # CORS
    config.include('.security.cors')
    config.add_cors_preflight_handler()

    # internal
    config.include('.models')
    config.include('.routes')
    config.scan('better_factory')

    # JWT
    # config.set_root_factory(RootACL)
    # config.set_authorization_policy(ACLAuthorizationPolicy())
    # config.set_jwt_authentication_policy(
    #     settings['jwt.secret'],
    #     auth_type='Bearer',
    #     expiration=60 * 60 * 24,  # 1 day
    #     callback=resolve_principals,
    # )

    # we have only API views
    config.set_default_csrf_options(require_csrf=False)
