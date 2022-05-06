FROM python:3.7-slim

RUN apt-get update && \
    apt-get install -y build-essential git openssh-client software-properties-common libpq-dev python3-dev
RUN mkdir -p -m 0600 ~/.ssh && ssh-keyscan gitlab.com >> ~/.ssh/known_hosts

WORKDIR /app

COPY requirements/base.txt /app/requirements/base.txt
COPY setup.py /app/setup.py

RUN --mount=type=ssh pip install -r requirements/base.txt
COPY . /app

EXPOSE 6543

ENTRYPOINT ["pserve"]