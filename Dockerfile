FROM python:3.10
ENV PYTHONUNBUFFERED 1
workdir /app

copy ./requirements.txt /app
run pip install -r requirements.txt
copy . .
cmd ["python", "./mysite/manage.py", "runserver", "0.0.0.0:8000"]
