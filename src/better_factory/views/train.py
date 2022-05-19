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
            config["task"]["save_path"] = f"data/models/{params['model']}"
            config["task"]["controls"] = params['input_tags']
            config["task"]["targets"] = [params['target_tag']]
            data_path = f"{tmpdirname}/df.csv"
            config["task"]["data_files"] = [data_path]
            if "training" in params:
                for key, value in params["training"].items():
                    config["training"][key] = value

            keys = params['data'][0].keys()
            with open(data_path, 'w', newline='') as output_file:
                dict_writer = csv.DictWriter(output_file, keys)
                dict_writer.writeheader()
                dict_writer.writerows(params['data'])
            
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
        