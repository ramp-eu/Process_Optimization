import logging
import csv
import tempfile

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
from bflab.interface import train, predict, optimize
from bflab.utils import (
    load_template, load_yaml, save_yaml
)

logger = logging.getLogger('better_factory')

class ModelApi(BaseApi):

    @view_config(
        route_name='model_api.predict',
        request_method='POST',
        openapi=True,
    )
    def predict(self):
        params = PredictInputSchema().load(self.request.json_body)
        # path where the model and the data frames are stored
        config = load_template('prediction')
        model_path = Path(f"data/models/{params['model']}")
        config['model_path'] = model_path

        with tempfile.TemporaryDirectory() as tmpdirname:
            data = params['data']
            keys = data[0].keys()
            with open(f"{tmpdirname}/data.csv", "w") as file:
                dict_writer = csv.DictWriter(file, keys)
                dict_writer.writeheader()
                dict_writer.writerows(data)
            config['data_path'] = file.name

            pred = predict(config)
            return PredictResponseSchema().dump({
                "predictions": pred['y'].to_list()
            })


    @view_config(
        route_name='model_api.optimize',
        request_method='POST',
        openapi=True,
    )
    def optimize(self):
        params = OptimizeInputSchema().load(self.request.json_body)
        config = load_template('optimization')
        model_path = Path(f"data/models/{params['model']}")
        config['model_path'] = model_path
        config["task"]['optim_limits'] = params["optim_limits"]
        config["task"]['setpoints'] = params["setpoints"]

        with tempfile.TemporaryDirectory() as tmpdirname:
            data = params['data']
            keys = data[0].keys()
            with open(f"{tmpdirname}/data.csv", "w") as file:
                dict_writer = csv.DictWriter(file, keys)
                dict_writer.writeheader()
                dict_writer.writerows(data)
            config['data_path'] = file.name

            opt = optimize(config)

            return OptimizeResponseSchema().dump({
                "optimizations": {
                    f"{tag}": opt[tag].tolist()[0]
                    for tag in opt.columns.tolist()
                }
            })
        