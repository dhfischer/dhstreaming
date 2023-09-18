#
#  DOCKERFILE
#
FROM python:3.7-slim-buster

# SET DOCKER PARAMETERS
ARG postgres_host=''

# SET ENVIRONMENT VARIABLES
# Enable real time logging
ENV PYTHONUNBUFFERED 1
ENV POSTGRES_HOST ${postgres_host}

RUN echo "Starting build"

# SET THE CODE DIRECTORY
WORKDIR /service

# COPY PYTHON DEPENDENCIES
COPY requirements.txt .

# INSTALL DEPENDENCIES
# - update system package manager
# - install system dependencies
# - update python package manager
# - install python project dependencies
# - cleanup
# && apt-get install -y unzip wget curl netcat nginx supervisor \
RUN set -ex \
    && apt-get update \
    && apt-get install -y unzip wget curl netcat \
    && pip --version \
    && python --version \
    && pip install --upgrade pip \
    && pip install --no-cache-dir gunicorn \
    && pip --version \
    && python --version \
    && pip install --no-cache-dir -r requirements.txt \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf /root/.cache \
    && find / -name "*.pyc" -exec rm -f {} \;

# COPY PROJECT FILES TO SERVICE DIRECTORY
COPY . .

# EXPOSE THE SERVICE PORT
EXPOSE 8000

# DEFINE THE DEFAULT COMMAND FOR STARTING THE CONTAINER
ENTRYPOINT ["/service/entrypoint.sh"]
