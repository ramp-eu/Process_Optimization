## Advanced optimization parameters

The following parameters are supported for optimizing the controls. Table below gives a short summary of the available parameters, and each parameter is explained in more detail after that.

| Parameter    | Required | Definition | Default |
| ------------ | -------- | ---------- | ------- |
| `optim_limits` | x        | Optimization limits for each control variable (i.e. model input) to be optimized. Controls for which limits are not specified will not be optimized.  | null        |
| `setpoints`    |          | Goal setpoints for target and/or control variables.        | null        |
| `limits_high`  |          | High limits for target and/or control variables.           | null        |
| `limits_low`   |          | Low limits for target and/or control variables.            | null        |

### `optim_limits`

`optim_limits` specifies limits (min, max) of the interval over which a particular control tag should be optimized. Only those control variables will be optimized for which the limits are specified. 

The table below specifies accepted parameters of each limit object.

| Parameter | Definition |
| --------- | ---------- |
| `min`       | Min value          |
| `max`       | Max value          |

```
Example:
{
    ...
    "optim_limits: {
        "x1": {
            "min": 0,
            "max": 10
        },
        "x2": {
            "min": 0,
            "max": 5
        },
        ...
    }
    ...
}

```



### `setpoints`

`setpoints` specifies setpoint information for a given target or control tag. Setpoints for target tags are used to steer the predicted variables towards a specific value, whereas setpoints for control variables can be used, for example, to regularize control optimization, or to minimize control applied.

The table below specifies accepted parameters of each setpoint object.

| Parameter | Definition |
| --------- | ---------- |
| `value`     | The setpoint value.           |
| `weight`    | The weight of this setpoint in the total optimization cost function.          |
| `loss_type` | Loss function that measures the deviation between the variable and its setpoint. Possible values: 1 (= L1 loss = max absolute deviation) or 2 (= L2 loss = squared deviation)            |
| `end_only`  | Whether the setpoint loss should be applied only at the end of the planning horizon, and not throughout the plan. E.g. if the prediction horizon of the model is 10 steps and `end_only = true`, then the setpoint loss will be applied only for the predicted value at step 10, not for the steps 1-9.           |

The example below attempts to optimize the model inputs so that target variable `y` would be steered towards value 5.0, and `x1` is regularized towards zero (relevant e.g. if there is a monetary cost associated that is proportional to the value of `x1`). Notice though that weight for this regularization is considerably lower than that of the setpoint for `y`, so higher priority is given for maintaining `y` around its goal setpoint.

```
Example:
{
    ...
    "setpoints": {
        "y": {
            "value": 5.0,
            "weight": 1.0,
            "loss_type": 2,
            "end_only": true
        },
        "x1": {
            "value": 0.0,
            "weight": 0.1,
            "loss_type": 1,
            "end_only": true
        }
    },
    ...
}
```



### `limits_high` and `limits_low`

`limits_high` and `limits_low` can be used to specify soft high and low limits for certain target and/or control tags. The logic is exactly the same as with `setpoints`, the only difference is that `limits_high` will not introduce any penalty if a variable obtains lower value, and `limits_low` will not introduce any penalty if the value is larger than that.

The table below specifies accepted parameters.

| Parameter | Definition |
| --------- | ---------- |
| `value`     | The high or low limit.           |
| `weight`    | The weight of this limit in the total optimization cost function.          |
| `loss_type` | Loss function that measures the deviation between the variable and its high/low limit. Possible values: 1 (= L1 loss = max absolute deviation) or 2 (= L2 loss = squared deviation)            |
| `end_only`  | Whether the high/low limit loss should be applied only at the end of the planning horizon, and not throughout the plan. E.g. if the prediction horizon of the model is 10 steps and `end_only = true`, then the high/low limit loss will be applied only for the predicted value at step 10, not for the steps 1-9.           |

The example below attempts to optimize the model inputs so that predicted value for the target variable `y` would not go below 5.0, and there is also a less strict upper limit of 10.0 (notice the smaller weight for the upper limit than for the lower limit). Again, `x1` is regularized towards zero. This essentially means that the optimization will find the smallest value of `x1` such that the predicted value of `y` remains between 5.0 ... 10.0.

```
Example:
{
    ...
    "limits_low": [
        "y": {
            "value": 5.0,
            "weight": 1.0,
            "loss_type": 2,
            "end_only": true,
        }
    ],
    "limits_high": [
        "y": {
            "value": 10.0,
            "weight": 0.1,
            "loss_type": 2,
            "end_only": true,
        }
    ],
    "setpoints": {
        "x1": {
            "value": 0.0,
            "weight": 0.01,
            "loss_type": 1,
            "end_only": true,
        }
    },
    ...
}
```
