# Let's Learn Django

## Introduction

I've started to work with Django when I first encountered with World Wide Web (WWW) for writing a web application for Sharif Energy Water Nexus Event, which is available [here](https://github.com/Panamo/EnerWat).
Since then, I use Go more than Python, so I need to refresh my memory and also celebrate my great memories with [Mohammad Mahboubi](https://github.com/mrma95) and [Navid Mashayekhi](https://github.com/navidmsk).

## Where did it start?

you need first create your django project:

```bash
django-admin startproject django101
```

and then you can create applications:

```bash
python manage.py startapp blog
```

please note that you need to write down the applications in `/django101/settings.py`
under the variable named `INSTALLED_APPS`.

## How to run?

This application is very simple so it uses [SQLite](https://www.sqlite.org/index.html).

```bash
pipenv install
pipenv shell
```

```bash
python manage.py migrate
python manage.py runserver
```

For working with database you can use [litecli](https://github.com/dbcli/litecli) which is available as a development package.

```bash
python manage.py createsuperuser
```

## On Production :rocket

For running Django on production it is better to use [gunicorn](https://gunicorn.org/).

```bash
gunicorn django101.wsgi --log-file -
```
