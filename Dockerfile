FROM python:3-alpine

RUN apk --no-cache add build-base

WORKDIR /app

RUN pip install --no-cache-dir --upgrade pipenv \
  && pipenv install --system

# cleanup the apk cache
RUN rm -rf /var/cache/apk/*

EXPOSE 8080

ENTRYPOINT ["python", "manage.py", "migrate", "&&", "gunicorn", "django101.wsgi", "--log-file", "-"]
