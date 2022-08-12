import logging
import shutil
import tempfile
import csv
import matplotlib
matplotlib.use('Agg')


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

from bflab.interface import train
from bflab.utils import (
    load_template, load_yaml, save_yaml
)

logger = logging.getLogger('better_factory')

class TrainApi(BaseApi):

    @view_config(
        route_name='train_api.queue',
        request_method='POST',
        openapi=True,
    )
    def queue(self):
        params = TrainInputSchema().load(self.request.json_body)
        config = load_template('training')

        with tempfile.TemporaryDirectory() as tmpdirname:
            config["model"]["class"] = params.get('model_class', "SeqNLDS")
            config["task"]["horizon_past"] = params["horizon_past"]
            config["task"]["horizon_future"] = params["horizon_future"]
            config["task"]["save_path"] = f"data/models/{params['model']}"
            config["task"]["controls"] = params['input_tags']
            config["task"]["targets"] = [params['target_tag']]
            config["task"]["data_files"] = []
            if "training" in params:
                for key, value in params["training"].items():
                    config["training"][key] = value

            for data_idx, data in enumerate(params['datasets']):
                data_path = f"{tmpdirname}/df{data_idx}.csv"
                keys = data[0].keys()
                with open(data_path, 'w', newline='') as output_file:
                    dict_writer = csv.DictWriter(output_file, keys)
                    dict_writer.writeheader()
                    dict_writer.writerows(data)

                config["task"]["data_files"].append(data_path)

            
            config_path = f"{tmpdirname}/config.yaml"
            save_yaml(config, config_path)
            config = load_yaml(config_path)
            train(config)

            return TrainResponseSchema().dump({
                "model": params['model'],
                "status": "available",
            })


    # @view_config(
    #     route_name='train_api.fetch',
    #     request_method='GET',
    #     openapi=True,
    # )
    # def fetch(self):
    #     params = self.request.openapi_validated.parameters.query
    #     model = params.get("model", None)

    #     return TrainResponseSchema().dump({
    #         "model": "test",
    #         "status": "available",
    #     })
        