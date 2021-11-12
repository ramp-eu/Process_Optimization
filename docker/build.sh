#!/bin/bash

DOCKER_BUILDKIT=1 docker build --ssh default "$@" -f docker/Dockerfile