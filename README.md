Garden Gnome
# Features

## Existing Features

# Admin 
To access admin the superusers details are
User: admin
Email: admin@gmail.com
Password: adminaccess

## Features Left to Implement

## Design Stage



# Testing

## Validator Testing

## Development Bugs
Comments not showing

Heroku not laoding css - believe static files not being located properly however url looks correct.

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

- Go to Heroku.com
    - Open account and create new app by clicking 'new'
    - In Deploy tab click connect to Github, search for correct repo
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
- Add DISABLE_COLLECTSTATIC to Heroku with the value set as 1 - this is required as there are no static files at present and will be removed later in the project

- In Settings.py connect Cloudinary database
    - Add cloudinary_storage to INSTALLED_APPS above django.contrib.staticfiles
    - Add cloudinary to INSTALLED_APPS underneith
    - under STATIC_URL add these lines
        - STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
        - STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
        - STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
        - DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
    - under Build paths section add TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
    - in TEMPLATES section add TEMPLATES_DIR as the value to the key 'DIRS':
    - in ALLOWED_HOSTS section add the Herolu app name and .herokuapp.com to the key value and localhost - this app's key will be ['garden-gnome-blog.herokuapp.com', 'localhost'] as an example
- Cretae Media, static and templates folders in the top level of our project on git

- Create a Procfile (must use a capital P) for Heroku to read
    - add web: gunicorn gardengnome.wsgi to Procfile

# Credits

Useful websites and tutorials 
https://djangocentral.com/building-a-blog-application-with-django/
https://www.youtube.com/watch?v=B40bteAMM_M&list=PLCC34OHNcOtr025c1kHSPrnP18YPB-NFi&ab_channel=Codemy.com
https://www.samuelliedtke.com/blog/implement-comment-system-blog-application-django/#views

Bootstrap 
https://www.youtube.com/watch?v=qNifU_aQRio&ab_channel=AdrianTwarog

## Content

pexels.com
googlefonts.com
fontawesome.com
pexels.com

## Media