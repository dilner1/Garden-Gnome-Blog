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

- create project using Django (this will be called gardengnome) with command django-admin startproject gardengnome .

- create app (this will be called blog) using command python3 manage.py startapp blog
- add blog to installed apps in settings.py
- migrate changes using python3 manage.py migrate (you should be able to view the django installed app succes page when runng the server using python3 manage.py runserver)


- Open Heroku account and create new app by clicking 'new'
- In Deploy tab click connect to Github, find correct repo
- Enable automatic deploys (this is optional)
- In Resouces tab search for Heroku Postgres and add, this will give you your DATABASE_URL which can be found in the settings section under Config Vars

- Back in git create create an env.py file, import os and add the postgres DATABASE_URL key 
- add a SECRET_KEY variable to env.py with a random key, back in Heroku add this to config vars - you will need to put SECRET_KEY in the key section and the random key in the value section, then press add
- We need to reference the env.py file in the settings.py file, in settings.py import os and import dj_database_url, then reference the env.py with an if statement
- update SECRET_KEY in settings.py or add it if not already present
- Go to DATABASES section in setting.py and set default to BATABASE_URL - the database will now be connected correctly with Heroku (this will be adjusted later but for now this will be fine)
- Migrate with python3 manage.py migrate
- Open Cloudinary account if you do not already have one, on the Dashboard there will be a API Environment Variable, click the copy to clipboard icon in the bottom right hand corner
- Paste into the env.py file, following the format for the other keys seperate CLOUDINARY_URL as the key nmae, remove the '=' and use the ramaining part as the key value
- Copy the Cloudinary url key name and value into config vars on Heroku as with the SECRET_KEY


# Credits

## Content

## Media