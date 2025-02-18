FROM python:3.8

WORKDIR /app

COPY django-test-web-server/requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY django-test-web-server// .

EXPOSE 8000

WORKDIR /app/django_test_web_server

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
