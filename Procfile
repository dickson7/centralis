release: python manage.py makemigrations
release: python manage.py migrate

web: gunicorn centralis_site.wsgi
