def includeme(config):
    api_base = '/api/v1.0'

    # openapi
    config.pyramid_openapi3_spec(
        "openapi.yaml",
        route=f"{api_base}/openapi.yaml",
    )
    config.pyramid_openapi3_add_explorer(route=f"{api_base}/")

    # auth
    # config.add_route('auth_api.login', f'{api_base}/login/')

    config.add_route('model_api.predict', f'{api_base}/model/predict/')
    config.add_route('model_api.optimize', f'{api_base}/model/optimize/')

    # config.add_route('train_api.upload', f'{api_base}/train/upload/')
    config.add_route('train_api.queue', f'{api_base}/train/queue/')
    config.add_route('train_api.fetch', f'{api_base}/train/fetch/')
    config.add_route('train_api.download', f'{api_base}/train/download/')
