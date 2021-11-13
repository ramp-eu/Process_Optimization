FROM python:3.7-slim

RUN apt-get update && \
    apt-get install -y git openssh-client software-properties-common
RUN mkdir -p -m 0600 ~/.ssh && ssh-keyscan gitlab.com >> ~/.ssh/known_hosts

WORKDIR /app

COPY src/requirements/base.txt /app/requirements/base.txt
COPY src/setup.py /app/setup.py

RUN --mount=type=ssh pip install -r requirements/base.txt
COPY src/. /app
COPY docker/entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

COPY src/config/production.ini.example /app/config/production.ini

EXPOSE 6543

ENTRYPOINT ["/app/entrypoint.sh"]