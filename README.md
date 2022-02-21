Garden Gnome
# Features

## Existing Features

## Features Left to Implement

# Testing

## Validator Testing

## Unfixed Bugs

# Deployment
- Create git repository from Code institute template
- Install required modules:
    - pip3 install Django==3.2 gunicorn
    - pip3 install dj_database_url psycopg2
    - pip install cloudinary (this is to store images for Heroku)
    - pip install dj3-cloudinary-storage
    - pip3 install django-allauth
    - pip3 install Django-crispy-forms
    - cp -r ../.pip-modules/lib/python3.8/site-packages/allauth/templates/* ./templates
- add to requirements.txt using (pip3 freeze —local > requirements.txt)
- Open Heroku account and create new app by clicking 'new'
- In Deploy tab click connect to Github, find correct repo
- Enable automatic deploys (this is optional)
- In Resouces tab search for Heroku Postgres and add, this will give you your DATABASE_URL which can be found in the settings section under Config Vars

- create project using Django (this will be called gardengnome) with command django-admin startproject gardengnome .

- create app (this will be called blog) using command python3 manage.py startapp blog
- add blog to installed apps in settings.py
- migrate changes using python3 manage.py migrate (you should be able to view the django installed app succes page when runng the server using python3 manage.py runserver)

# Credits

## Content

## Media