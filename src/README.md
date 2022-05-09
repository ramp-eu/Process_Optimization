### Getting started

```
COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 DOCKER_DEFAULT_PLATFORM=linux/amd64 docker-compose up --build -d
```

### Releasing to RAMP

```
echo "$LOGIN_SECRET" | docker login --username duc.ta --password-stdin docker.ramp.eu

alias dc-ramp="COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 DOCKER_DEFAULT_PLATFORM=linux/amd64 docker-compose"
dc-ramp build --no-cache

docker push docker.ramp.eu/tds-pvt/pserve:latest
```
