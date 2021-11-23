import logging

from pyramid.view import view_config
from sqlalchemy.orm import joinedload

from pathlib import Path
import pandas as pd
import aiya_seqmod
from aiya_seqmod.data.preprocess import IdentityPreprocessor
from aiya_seqmod.interface import ModelManager



# from .. import models
from ..schemas.predict import (
    PredictInputSchema,
    PredictResponseSchema,
    OptimizeInputSchema,
    OptimizeResponseSchema,
)
from .base import BaseApi
from .exceptions import ApiError

logger = logging.getLogger('better_factory')

class PredictApi(BaseApi):

    @view_config(
        route_name='model_api.predict',
        request_method='POST',
        openapi=True,
    )
    def predict(self):
        params = PredictInputSchema().load(self.request.json_body)
        # path where the model and the data frames are stored
        model_path = Path(f"data/models/{params['model']}")
        data = params['data']

        # load the model
        model = aiya_seqmod.load(model_path)

        # create model manager
        # NOTE: here we use dummy preprocessor; in reality we would load a preprocessor-object
        # which was created at the time of model fitting, but let's ignore it for now...
        model_manager = ModelManager(model, IdentityPreprocessor())

        # load some mock-up data, that simulates real sensor data from an online process
        df = pd.read_pickle(Path(f"data/df_test.pkl"))

        # make prediction given the latest online data
        pred = model_manager.predict(df)['y']
        return PredictResponseSchema().dump({
            "predictions": pred.to_list(),
        })


    @view_config(
        route_name='model_api.optimize',
        request_method='POST',
        openapi=True,
    )
    def optimize(self):
        params = OptimizeInputSchema().load(self.request.json_body)
        tags = params["tags"]

        return OptimizeResponseSchema().dump({
            "optimizations": {
                f"{tag}": 2.0
                for tag in tags
            }
        })
        