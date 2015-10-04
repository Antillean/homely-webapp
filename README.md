# homely-webapp
Homely RESTful webapp for c4tk

# Getting Started

## Pre-Requisites

The only pre-requisites for this project are:

1. Python 2.7+ or Python 3.4+
1. pip
1. virtualenv

## Installation steps

### Setting up Python

1. Clone the repository.
1. Create a virtual environment with `virtualenv venv`.
1. Activate the virtual environment with `source venv\bin\activate` on \*nix or `.\venv\Scripts\activate` on Windows.
1. Install the required packages with `pip install -r requirements.txt`. (NB: I haven't been able to get Windows to install a working version of psycopg2. With Python 2.7 [the Microsoft Visual C++ Compiler for Python 2.7](https://www.microsoft.com/en-gb/download/details.aspx?id=44266) stopped pip from complaining, but then Django seemed unhappy with what pip installed. I haven't tried what's required for Python 3.)

### Setting up PostgreSQL locally

1. [Download and install PostgreSQL server](http://www.postgresql.org/download/) for your platform.
1. Run postgres.
1. Using the commandline or [pgadmin](http://www.pgadmin.org/), create a user `pyhomely` and give it permissions to create databases.
1. Create a file `homely/local_settings.py`, and put something like this in it.

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

3. Setup the db by running `python manage.py migrate`.
3. You might also want to create a super user for use in the admin console and rest interface with `python manage.py createsuperuser`.
