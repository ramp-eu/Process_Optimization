import json
import csv
import requests


def request(action, payload, *, method="POST", **kwargs):
    url = {
        "train": "http://localhost:6543/api/v1.0/train/queue/",
        "fetch_train": "http://localhost:6543/api/v1.0/train/fetch/",
        "download_train": "http://localhost:6543/api/v1.0/train/download/",
        "predict": "http://localhost:6543/api/v1.0/model/predict/",
        "optimize": "http://localhost:6543/api/v1.0/model/optimize/"
    }[action]
    headers = {
        'Authorization': 'Bearer testoken',
        'Content-Type': 'application/json'
    }
    params = payload if method == "GET" else None
    data = json.dumps(payload) if method == "POST" else None
    return requests.request(
        method, url,
        headers=headers,
        params=params,
        data=data,
        **kwargs,
    )


def read_csv(filename):
    with open(filename) as f:
        return [
            {k: float(v) if k != 'time' else v for k, v in row.items()} 
            for row in csv.DictReader(f, skipinitialspace=True)
        ]

if __name__ == "__main__":
    model_name = "testmodel"
    train_df = read_csv("df1.csv")
    df = read_csv("df2.csv")

    response = request("train", {
        "model": model_name,
        "input_tags": ["x1", "x2"],
        "target_tags": ["y"],
        "model_class": "NLDS",
        "horizon_past": 15,
        "horizon_future": 5,
        "time_discretization": "1min",
        "datasets": [
            train_df
        ]
    })
    print(response.text)

    response = request("fetch_train", {
        "model": model_name,
    }, method="GET")
    print(response.text)

    response = request("download_train", {
        "model": model_name,
    })
    download_path = f"./{model_name}.zip"
    with open(download_path, 'wb') as f:
        f.write(response.content)
    print(f"Downloaded to {download_path}")

    response = request("predict", {
        "model": model_name,
        "data": df,
    })
    print(response.text)

    response = request("optimize", {
        "model": model_name,
        "optim_limits": {
            "x1": {
                "min": -2,
                "max": 2
            },
            "x2": {
                "min": -2,
                "max": 2
            }
        },
        "setpoints": {
            "y": {
                "value": 5.0,
                "weight": 1.0,
                "loss_type": 2,
                "end_only": False
            }
        },
        "data": df,
    })
    print(response.text)