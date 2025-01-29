<h1 align="center">Let's Learn Django</h1>

<h6 align="center">Django makes it easier to build better web apps more quickly and with less code</h6>

<p align="center">
  <img src="https://img.shields.io/github/actions/workflow/status/1995parham-learning/django101/test.yaml?label=ci&logo=github&style=for-the-badge&branch=main" alt="GitHub Workflow Status">
  <img alt="GitHub" src="https://img.shields.io/github/license/1995parham-learning/django101?logo=gnu&style=for-the-badge">
</p>

## Introduction

I've started to work with Django when I first encountered with World Wide Web (WWW) for writing a web application for Sharif Energy Water Nexus Event, which is available [here](https://github.com/Panamo/EnerWat).
Since then, I use Go more than Python, so I need to refresh my memory and also celebrate my great memories with [Mohammad Mahboubi](https://github.com/mrma95) and [Navid Mashayekhi](https://github.com/navidmsk).

## Where did it start?

You need first create your Django project:

```bash
pipx run --spec django==4.2.5 django-admin startproject django101
```

and then you can create applications:

```bash
python manage.py startapp blog
```

Please note that you need to write down the applications in `/django101/settings.py`
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

## Better development experience

Having a good language server is an awesome experience that every developer wants.
[Pyright](https://github.com/microsoft/pyright) seems a good choice to me and for having it work with Django, you can:

```bash
pipenv install --dev  'django-stubs[compatible-mypy]'
```

And then you must register it to mypy by add the following into `mypy.ini`:

```ini
[mypy]
plugins =
    mypy_django_plugin.main

[mypy.plugins.django-stubs]
django_settings_module = "django101.settings"
```

Maybe you want to use [django-rest-framework](https://www.django-rest-framework.org/) too for having an awesome ReST API.

```bash
pipenv install --dev 'djangorestframework-stubs[compatible-mypy]'
```

```ini
[mypy]
plugins =
    mypy_django_plugin.main, mypy_drf_plugin.main
```

## On Production 🚀

For running Django on production it is better to use [gunicorn](https://gunicorn.org/).

```bash
gunicorn django101.wsgi --log-file -
```
