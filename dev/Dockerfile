FROM python:3.11

ENV PYTHONUNBUFFERED 1

RUN /bin/sh -c set -ex; apt-get update; \
    apt-get install -y --no-install-recommends \
    binutils \
    gettext \
    libproj-dev \
    gdal-bin

WORKDIR /code
RUN mkdir -p /code/requirements
COPY ./requirements/requirements.txt /code/requirements/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements/requirements.txt
COPY ./ /code/

CMD ["bash"]
