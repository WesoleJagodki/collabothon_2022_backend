
run:
	python ./mysite/manage.py runserver

makemigrations:
	python ./mysite/manage.py makemigrations

migrate:
	python ./mysite/manage.py migrate

createsuperuser:
	python ./mysite/manage.py createsuperuser --username admin --email admin@admin.pl

