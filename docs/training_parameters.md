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
| fraction_validation          |            | 0.2     |
| learning_rate                |            | 0.001   |
| learning_momentum            |            | 0.9     |
| learning_rate_decay_interval |            | 2000    |
| learning_rate_decay_factor   |            | 0.5     |
| num_training_epochs          |            | null    |
| num_training_steps           |            | 10000   |
| max_grad_norm                |            | 100.0   |
| batch_size                   |            | 32      |
| seed                         |            | 42      |
