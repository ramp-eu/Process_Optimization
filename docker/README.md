### Running the module

```
echo "$LOGIN_SECRET" | docker login --username username --password-stdin docker.ramp.eu

docker-compose up -d
```

Then continue with code example with test data: https://github.com/ramp-eu/Process_Optimization/blob/master/docker/examples/main.py

The example can be used as reference for later implementation or to test the pipeline with real data.
