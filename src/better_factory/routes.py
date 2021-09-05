def includeme(config):
    api_base = '/api/v1.0'

    # auth
    # config.add_route('auth_api.login', f'{api_base}/login/')

    # user
    config.add_route('predict_api.predict', f'{api_base}/predict/')

    # mill, metadata only, not in use at the moment