import logging

from pyramid.view import view_config
from sqlalchemy.orm import joinedload

from pathlib import Path
import pandas as pd
import aiya_seqmod
from aiya_seqmod.data.preprocess import IdentityPreprocessor
from aiya_seqmod.interface import ModelManager



# from .. import models
from ..schemas.train import (
    TrainInputSchema,
    TrainResponseSchema
)
from .base import BaseApi
from .exceptions import ApiError

logger = logging.getLogger('better_factory')

class TrainApi(BaseApi):

    @view_config(
        route_name='train_api.queue',
        request_method='POST',
        openapi=True,
    )
    def queue(self):
        params = TrainInputSchema().load(self.request.json_body)

        # TODO: start the training process
        
        return TrainResponseSchema().dump({
            "model": "mockup",
            "status": "available",
        })


    @view_config(
        route_name='train_api.fetch',
        request_method='GET',
        openapi=True,
    )
    def fetch(self):
        params = self.request.openapi_validated.parameters.query
        model = params.get("model", None)

        return TrainResponseSchema().dump({
            "model": "mockup",
            "status": "available",
        })
        