# pull official base image
FROM python:3.11.3-slim-buster

# Install PostgreSQL client, development libraries, and build tools
RUN apt-get update \
    && apt-get install -y postgresql-client libpq-dev build-essential \
    && rm -rf /var/lib/apt/lists/*

# Set work directory
WORKDIR /usr/src/app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

# Copy project
COPY . /usr/src/app/
