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

| Parameter                    | Definition | Default |
| ---------------------------- | ---------- | ------- |
| `fraction_validation`          | Fraction of data that is assigned to the validation set.  | 0.2     |
| `learning_rate`                | Learning rate for the stochastic gradient descent.        | 0.001   |
| `learning_momentum`            | Momentum for the stochastic gradient descent.           | 0.9     |
| `learning_rate_decay_interval` | Number of training steps after which the learning rate is always decreased by a factor `learning_rate_decay_factor`. | 2000    |
| `learning_rate_decay_factor`   | Factor by which the learning rate is always decreased after every `learning_rate_decay_interval` steps.  | 0.5     |
| `num_training_epochs`          | Number of training epochs. If not given, then the number of epochs will be decided by a minimum number of training steps, see `num_training_steps`. | null    |
| `num_training_steps`           | Minimum number of training steps (or iterations). The total number of training steps is decided so that the last epoch will always be completed. If the `num_training_epochs` is given, then this value will be ignored.       | 10000   |
| `max_grad_norm`                | Maximum value for the gradient norm. Used to avoid instability during training due to exploding gradients. | 100.0   |
| `batch_size`                   | Batch size for the stochastic gradient descent.  | 32      |
| `seed`                         | Random seed for reproducible results.  | 42      |
