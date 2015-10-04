# homely-webapp
Homely RESTful webapp for c4tk

# Getting Started

## Pre-Requisites

The only pre-requisites for this project are:

1. [Python 2.7+ or Python 3.4+](https://www.python.org/downloads/)
1. On Linux: python-dev
1. [pip](http://pip.readthedocs.org/en/latest/installing/)
1. [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/)

## Installation steps

### Setting up Python

1. Clone the repository.
1. In a terminal window in your local copy of the repo, create a virtual environment with `virtualenv venv`.
1. Activate the virtual environment with `source venv/bin/activate` on \*nix or `.\venv\Scripts\activate` on Windows.
1. Install the required packages with `pip install -r requirements.txt`. (NB: I haven't been able to get Windows to install a working version of psycopg2. With Python 2.7 [the Microsoft Visual C++ Compiler for Python 2.7](https://www.microsoft.com/en-gb/download/details.aspx?id=44266) stopped pip from complaining, but then Django seemed unhappy with what pip installed. I haven't tried what's required for Python 3.)

### Setting up PostgreSQL locally

1. [Download and install PostgreSQL server](http://www.postgresql.org/download/) for your platform.
1. Start postgres in a way appropriate for your platform.
1. Using the terminal or [pgadmin](http://www.pgadmin.org/):
  1. Create a user `pyhomely` with password `pyhomely`.
  1. Create a database `homely` owned by user `pyhomely`.
1. Make a file called `homely/local_settings.py`. The easiest way to do that is to copy `homely/local_settings.py.template`, rename the copy to `local_settings.py`, and edit it as you need to.
1. Run `python manage.py migrate` to setup the db.
1. You might also want to create a super user for use in the admin console and rest interface with `python manage.py createsuperuser`.
1. Go to http://localhost:8000/api/ to see the api running locally on your machine!
