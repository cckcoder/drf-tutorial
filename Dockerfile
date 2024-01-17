FROM python:3.10.11-slim-buster

# Location of source code
WORKDIR /app
# Copying requirements
COPY requirements.txt .

ENV PYTHONUNBUFFERED 1
# Install OS Library for Python Package
RUN apt-get update && apt-get install -y gettext
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install -r requirements.txt

# Copy Source File
COPY . .
