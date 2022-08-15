## Common training parameters

| Parameter             | Definition                                                                                                                                                                                                                                                                                                                                                                      | Default   |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| `model`               | Name of the model.                                                                                                                                                                                                                                                                                                                                                              | required  |
| `input_tags`          | Names of the controllable tags/inputs.                                                                                                                                                                                                                                                                                                                                          | required  |
| `target_tags`         | Name(s) of the tags to predict. NOTE: currently only one target tag is supported (multiple tags will be implemented in the future).                                                                                                                                                                                                                                             | required  |
| `datasets`            | List of datasets used for training                                                                                                                                                                                                                                                                                                                                              | required  |
| `time_discretization` | Discretization interval between two consecutive time steps for the model. If the original data has more frequent measurements than this, then the data will be downsampled averaging measurements within each interval. The value should be a string that can be converted to time delta using `pandas.to_timedelta(time_discretization)`, e.g. "1s", "1min", "5min", "1h" etc. | required  |
| `horizon_past`        | Number of past time steps taken into account when forecasting the future.                                                                                                                                                                                                                                                                                                       | required  |
| `horizon_future`      | Number of time steps the model should forecast into the future.                                                                                                                                                                                                                                                                                                                 | required  |
| `model_class`         | Model architecture (see options below).                                                                                                                                                                                                                                                                                                                                         | NLDS      |
| `training`            | Advanced/detailed hyperparameters regarding the model training, see details below.                                                                                                                                                                                                                                                                                              | See below |

## Model Classes

Available models are listed below:

| Model Class | Definition                                            |
| ----------- | ----------------------------------------------------- |
| "Linear"    | Autoregressive linear model                           |
| "MLP"       | Autoregressive non-linear multilayer perceptron model |
| "CNN"       | Autoregressive convolutional neural network model     |
| "NLDS"      | Non-linear dynamical system model                     |


## Advanced training parameters

The following training parameters are supported, and can be passed under key `training`.

```
{
    ...
    "training": {
        "fraction_validation": 0.2
    }
}

```

| Parameter                      | Definition                                                                                                                                                                                                               | Type                    | Default |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------- | ------- |
| `fraction_validation`          | Fraction of data that is assigned to the validation set.                                                                                                                                                                 | float (between 0 and 1) | 0.2     |
| `learning_rate`                | Learning rate for the stochastic gradient descent.                                                                                                                                                                       | float                   | 0.001   |
| `learning_momentum`            | Momentum for the stochastic gradient descent.                                                                                                                                                                            | float (between 0 and 1) | 0.9     |
| `learning_rate_decay_interval` | Number of training steps after which the learning rate is always decreased by a factor `learning_rate_decay_factor`.                                                                                                     | int                     | 2000    |
| `learning_rate_decay_factor`   | Factor by which the learning rate is always decreased after every `learning_rate_decay_interval` steps.                                                                                                                  | float (between 0 and 1) | 0.5     |
| `num_training_epochs`          | Number of training epochs. If not given, then the number of epochs will be decided by a minimum number of training steps, see `num_training_steps`.                                                                      | int                     | null    |
| `num_training_steps`           | Minimum number of training steps (or iterations). The total number of training steps is decided so that the last epoch will always be completed. If the `num_training_epochs` is given, then this value will be ignored. | int                     | 10000   |
| `max_grad_norm`                | Maximum value for the gradient norm. Used to avoid instability during training due to exploding gradients.                                                                                                               | float                   | 100.0   |
| `batch_size`                   | Batch size for the stochastic gradient descent.                                                                                                                                                                          | int                     | 32      |
| `seed`                         | Random seed for reproducible results.                                                                                                                                                                                    | int                     | 42      |
