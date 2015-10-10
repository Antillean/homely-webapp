# homely-webapp
Homely RESTful webapp for c4tk

# Getting Started

These instructions should work on Ubuntu 15.04 (Vivid Vervet) and Mac OS X Yosemite. I can't vouch for other \*nix OSes.

I couldn't get this to work on Windows, so if you're on Windows (as I often am) I suggest you run Ubuntu in VirtualBox.

## Pre-Requisites

1. [Python 2.7+ or Python 3.4+](https://www.python.org/downloads/)
1. The Python developer package on Linux. Get it with `sudo apt-get install python-dev` on Ubuntu or a similar, appropriate command for your Linux distro (such as `sudo yum install python-devel` [on CentOS](http://stackoverflow.com/questions/23541205/cant-install-python-dev-on-centos-6-5)).
1. [pip](http://pip.readthedocs.org/en/latest/installing/)
1. [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/)

## Installation steps

### Setting up Python

1. Clone the repository.
1. In a terminal window in your local copy of the repo, create a virtual environment with `virtualenv venv`.
1. Activate the virtual environment with `source venv/bin/activate`.
1. Install the required packages with `pip install -r requirements.txt`.

### Setting up PostgreSQL locally

1. [Download and install PostgreSQL server](http://www.postgresql.org/download/) for your platform.
1. Start postgres.
1. Using the terminal or [pgadmin](http://www.pgadmin.org/):
  1. Create a user `pyhomely` with password `pyhomely`.
  1. Create a database `homely` owned by that user `pyhomely`.
1. Make a file called `homely/local_settings.py`. The easiest way to do that is to copy `homely/local_settings.py.template`, rename the copy to `local_settings.py`, and edit it as you need to.
1. Run `python manage.py migrate` to setup the db.
1. You might also want to create a super user for use in the admin console and rest interface with `python manage.py createsuperuser`.
1. Go to http://localhost:8000/api/ to see the api running locally on your machine!
