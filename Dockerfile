######## BUILDER ########
FROM python:3.11-slim-bullseye as requirements-stage
WORKDIR /tmp
RUN pip install poetry
COPY ./pyproject.toml ./poetry.lock* /tmp/
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes


######## RUNNER ########
FROM python:3.11-slim-bullseye
# update security
# download latest listing of available packages:
RUN apt-get -y update \
    && apt-get -y upgrade \
    && rm -rf /var/lib/apt/lists/*
# add non-root user
RUN useradd --create-home appuser
# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# install dependencies
COPY --from=requirements-stage /tmp/requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /tmp/requirements.txt
# user
USER appuser
# set work directory
WORKDIR /home/appuser/app
# set pythonpath
ENV PYTHONPATH="/home/appuser/"
# copy project
COPY ./app /home/appuser/app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]