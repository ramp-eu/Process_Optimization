import logging
import shutil
import tempfile
import csv
import os
import shutil
import traceback
from contextlib import redirect_stdout

import matplotlib
from pyramid.view import view_config
from pyramid.response import Response, FileResponse
from sqlalchemy.orm import joinedload

from pathlib import Path
import pandas as pd
import aiya_seqmod
from aiya_seqmod.data.preprocess import IdentityPreprocessor
from aiya_seqmod.interface import ModelManager

matplotlib.use('Agg')


# from .. import models
from ..schemas.train import (
    TrainDownloadSchema,
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
            config["model"]["class"] = params.get('model_class', "NLDS")
            config["task"]["horizon_past"] = params["horizon_past"]
            config["task"]["horizon_future"] = params["horizon_future"]
            config["task"]["save_path"] = f"data/models/{params['model']}"
            config["task"]["controls"] = params['input_tags']
            config["task"]["targets"] = params['target_tags']
            config["task"]["data_files"] = []
            config["task"]["time_discretization"] = params["time_discretization"]
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
            is_error = False 
            training_logs = ""
            with open(f"data/models/{params['model']}/training_logs.txt", 'w') as f:
                with redirect_stdout(f):
                    print(f"Start training model: {params['model']}")
                    try:
                        train(config)
                    except:
                        print(traceback.format_exc())
                        is_error = True
                        
            
            if is_error:
                try:
                    with open(f"data/models/{params['model']}/training_logs.txt", "r") as f:
                        training_logs = f.readlines()
                except FileNotFoundError:
                    raise ApiError('Training log is not available.', status=400)

                return TrainResponseSchema().dump({
                    "model": params['model'],
                    "status": "error",
                    "training_logs": training_logs,
                })

            return TrainResponseSchema().dump({
                "model": params['model'],
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
        training_logs = ""
        try:
            with open(f"data/models/{params['model']}/training_logs.txt", "r") as f:
                training_logs = f.readlines()
        except FileNotFoundError:
            raise ApiError('Training log is not available.', status=400)

        status = "unavailable"
        if os.path.exists(f"data/models/{params['model']}/model_core.pt"):
            status = "available"

        return TrainResponseSchema().dump({
            "model": params['model'],
            "status": status,
            "training_logs": training_logs,
        })

    @view_config(
        route_name='train_api.download',
        request_method='POST',
        openapi=True,
    )
    def download(self):
        params = TrainDownloadSchema().load(self.request.json_body)
        model = params.get("model", None)

        if not os.path.exists(f"data/models/{model}/model_core.pt"):
            raise ApiError('Model is not available for downloading.', status=400)

        # base_dir = f"data/models"
        base_dir = f"/tmp"
        zip_name = f"{model}.zip"
        zip_output_path = f"{base_dir}/{model}"
        zip_path = f"{base_dir}/{model}.zip"
        shutil.make_archive(
            zip_output_path, 
            'zip', 
            f"data/models/{model}/"
        )

        response = Response(content_type='application/zip')
        response = FileResponse(str(zip_path))
        response.headers['Content-Disposition'] = (
            f'attachment; filename={zip_name}'
        )
        return response