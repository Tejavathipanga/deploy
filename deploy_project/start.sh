python manage.py migrate
python manage.py collectstatic --noinput
gunicorn 'deploy_project.wsgi.application'