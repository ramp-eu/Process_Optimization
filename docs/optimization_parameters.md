## Advanced optimization parameters

The following training parameters are supported, some parameters are required for the optimization process.

| Parameter    | Required | Definition | Default |
| ------------ | -------- | ---------- | ------- |
| optim_limits | x        |            |         |
| setpoints    | x        |            |         |
| limits_high  |          |            |         |
| limits_low   |          |            |         |

#### optim_limits

`optim_limits` specifies limits of controlling tags.

```
Example:
{
    ...
    "optim_limits: {
        "x1": {
            "min": -2,
            "max": 2
        },
        "x2": {
            "min": -2,
            "max": 2
        },
        ...
    }
    ...
}

```

The table below specifies accepted parameters of each limit object.

| Parameter | Definition |
| --------- | ---------- |
| min       |            |
| max       |            |

#### setpoints

`setpoints` specifies parameters of the target tag.

```
Example:
{
    ...
    "setpoints": {
        "y": {
            "value": 5.0,
            "weight": 1.0,
            "loss_type": 2,
            "end_only": False
        }
    },
    ...
}
```

The table below specifies accepted parameters of each target object.

| Parameter | Definition |
| --------- | ---------- |
| value     |            |
| weight    |            |
| loss_type |            |
| end_only  |            |

#### limits_high and limits_low

`limits_high` and `limits_low` specify parameters of the each tag.

```
Example:
{
    ...
    "limits_high": [
        "y": {
            "end_only": false,
            "loss_type": 2,
            "value": 6,
            "weight": 100.0
        },
        ...
    ],
    "limits_low": [
        "y": {
            "end_only": false,
            "loss_type": 2,
            "value": 4.0,
            "weight": 100.0
        },
        ...
    ],
    ...
}
```

The table below specifies accepted parameters.

| Parameter | Definition |
| --------- | ---------- |
| value     |            |
| weight    |            |
| loss_type |            |
| end_only  |            |
