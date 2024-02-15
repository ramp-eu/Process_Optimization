### Getting started

#### docker-compose

```
COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 DOCKER_DEFAULT_PLATFORM=linux/amd64  docker-compose up --build -d
```

#### docker

```
# To build the image (needs to be inside src subfolder):
DOCKER_BUILDKIT=1 DOCKER_DEFAULT_PLATFORM=linux/amd64 docker build -t docker.ramp.eu/tds-pvt/pserve:latest --ssh default .

# To run the image:
docker run --name pserve --volume source=.,target=/app -p 6543:6543 docker.ramp.eu/tds-pvt/pserve:latest /app/config/docker.ini --reload
```

### Releasing to RAMP

```
echo "$RAMP_LOGIN_SECRET" | docker login --username duc.ta --password-stdin docker.ramp.eu

alias dc-ramp="COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 DOCKER_DEFAULT_PLATFORM=linux/amd64 docker-compose"
dc-ramp build --no-cache

docker push docker.ramp.eu/tds-pvt/pserve:latest
```
