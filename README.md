# DRF Tutorial

## Setup ENV.

* Install env into project directory `python -m venv env`
* Then activate the env
    * For windows `env/Script/activate`
    * For Linux, Macos `source env/bin/activate`

## Install Django and Django RESTFramework.

* Install Django `pip install django`
* Install Django RESTFramework `pip install djangorestframework`

## Project Setup.

Create a project name mysite with this command.

`django-admin startproject mysite .`

Create an app with this command.

`django-admin startapp api`

## Makemigration and Migrate.

* First need to makemigrations to get migrate file `python manage.py makemigrations`
* Then migrate the model to DB with command `python manage.py migrate`

## Django Admin.

> Create Super user.

`python manage.py createsuperuser`

## CORS

Install the library `django-cors-headers`

* [Repo](https://github.com/adamchainz/django-cors-headers)

`python -m pip install django-cors-headers`

## Test

Create a test case example on `test.py` under the application.

Execute with this command

`python manage.py test`
