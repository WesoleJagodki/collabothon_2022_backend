FROM python:3.10
workdir /app

copy ./requirements.txt /app
run pip install -r requirements.txt
copy . ./app
cmd ["python", "./mysite/manage.py", "runserver"]
