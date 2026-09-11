# TODO: select a base image
# Tip: start with a full base image, and then see if you can optimize with
#      a slim or tensorflow base

#      Standard version
FROM python:3.12-trixie

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# create a work directory
WORKDIR /app

COPY pyproject.toml pyproject.toml
COPY uv.lock uv.lock

ENV UV_NO_DEV=1 \
    UV_FROZEN=1

# install dependencies
RUN uv sync

# Install requirements
#COPY requirements.txt requirements.txt
#RUN pip install --no-cache-dir --upgrade pip
#RUN pip install --no-cache-dir -r requirements.txt

# Copy our code
COPY api api
COPY artifacts artifacts
COPY src src

# Make directories that we need, but that are not included in the COPY
#RUN mkdir /raw_data
#RUN mkdir /models

# COPY credentials.json credentials.json

# TODO: to speed up, you can load your model from MLFlow or Google Cloud Storage at startup using
# RUN python -c 'replace_this_with_the_commands_you_need_to_run_to_load_the_model'

CMD ["sh", "-c", "uv run uvicorn api.fast:app --host 0.0.0.0 --port ${PORT:-8080}"]
