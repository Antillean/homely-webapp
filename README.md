# homely-webapp
Homely RESTful webapp for c4tk

# Getting Started

# Local DB
1. [Download and install PostgreSQL server](http://www.postgresql.org/download/) for your platform.
1. Using the commandline or [pgadmin](http://www.pgadmin.org/), create a user `pyhomely` and give it permissions to create databases.
1. Create a file `home/local_settings.py`, and put something like this in it.

  ```
  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.postgresql_psycopg2',
          'NAME': 'homely',
          'USER': 'pyhomely',
          'PASSWORD': 'pyhomely',
          'HOST': '127.0.0.1',
          'PORT': '5432',
      }
  }
  ```

3. Setup the db by running `python manage.py syncdb`.
