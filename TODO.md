# TODO List

    **Drop postgresql tables utilized by the project**
    $ cd ~/GitRepositories/flask-microservices-users
    $ source env/bin/activate
    (env) $ python manage.py db migrate
    (env) $ python manage.py db upgrade
    (env) $ python manage.py test
    --Tests should pass 