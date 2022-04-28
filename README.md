Garden Gnome
# Features

## Existing Features

The Site on multiple screen sizes
![ page](https://res.cloudinary.com/ddxxrzq7g/image/upload/v1651139368/responsive_design_hscdiq.png "responsive design image")

Home Page
includes sticky nav bar
![home page](https://res.cloudinary.com/ddxxrzq7g/image/upload/v1651139372/home_page_xfp8v9.png "home page image")

Sign up Page
![signup page](https://res.cloudinary.com/ddxxrzq7g/image/upload/v1651139362/signup_cmeotk.png "signup page image")

Sign in Page
![ page](https://res.cloudinary.com/ddxxrzq7g/image/upload/v1651139362/signin_iulddc.png "signin page image")

Sign out Page
![ page](https://res.cloudinary.com/ddxxrzq7g/image/upload/v1651139363/signout_vcxgub.png "signout page image")

Create Post Page
![ page](https://res.cloudinary.com/ddxxrzq7g/image/upload/v1651139776/create_post_g5m4i8.png "create post page image")

Comments and likes
![ page](https://res.cloudinary.com/ddxxrzq7g/image/upload/v1651139352/comments_likes_wmg31u.png "comments and likes image")

Update Email Page
![ page](https://res.cloudinary.com/ddxxrzq7g/image/upload/v1651139372/update_email_jymrtr.png "update email page image")

Update Password Page
![ page](https://res.cloudinary.com/ddxxrzq7g/image/upload/v1651139361/password_reset_ppdvg3.png "update password page image")

Delete Post Page
![ page](https://res.cloudinary.com/ddxxrzq7g/image/upload/v1651139360/delete_post_mo6br1.png "delete post page image")

# Admin 
To access admin the superusers details are
User: admin
Email: admin@gmail.com
Password: adminaccess

## Features Left to Implement

## Design Stage

# Database

Started with basic models for the user which will be handled by Djangos all auth, the post and comments models

User Test Model
![user test model](https://res.cloudinary.com/ddxxrzq7g/image/upload/v1651144441/user_test_model_eh6jvf.png "user test model image")

Post Test Model
![usposter test model](https://res.cloudinary.com/ddxxrzq7g/image/upload/v1651144441/post_test_model_dxgi6e.png "post test model image")

Comment Test Model
![comment test model](https://res.cloudinary.com/ddxxrzq7g/image/upload/v1651144441/comment_test_model_uhfmf1.png "comment test model image")

UX
1. Strategy
2. Scope
3. Structure
4. Skeleton
5. Surface

# Testing

## Validator Testing

CSS validator
![CSS validator](https://res.cloudinary.com/ddxxrzq7g/image/upload/v1650972090/css_validator_index_rc6glx.png "CSS validator")

HTML index page validator
![HTML index validator](https://res.cloudinary.com/ddxxrzq7g/image/upload/v1650972457/HTML_Index_Validator_lbitjw.png "HMTL index validator")

HTML add post page validator
![HTML add post validator](https://res.cloudinary.com/ddxxrzq7g/image/upload/v1650972461/HTML_Add_Post_Validation_mozpd7.png "HTML index validator")

HTML Profile validator
![HTML Profile validator](https://res.cloudinary.com/ddxxrzq7g/image/upload/v1651090456/HTML_Profile_Validator_bdyshi.png "HTML profile validator")

![HTML Logout validator](https://res.cloudinary.com/ddxxrzq7g/image/upload/v1650972715/HTML_logout_Validator_cmtgge.png "HTML logout validator")

![HTML Login validator](https://res.cloudinary.com/ddxxrzq7g/image/upload/v1650973140/HTML_Login_Validation_gozobo.png "HTML login validator")

## Development Bugs
- Link to Edit post breaking open_post.html - error = Reverse for 'edit_post' with no arguments not found.
- In urls.py in this order update/<slug:slug>
- Added post:slug to end of url link in open_post.html like this {% url 'edit_post' post.slug%}

- on sign in user is registered but error appears ConnectionRefusedError at /accounts/signup/
[Errno 111] Connection refused
- Issue not clear but stack overflow suggests there is an error trying to send an email
- Setting dummy email backend in settings removes issue and directs user back to main page as it should

Comments not showing
- Comments not showing even tho they appear in admin panel and approved
- Removed {% if not comment in comments %}, realised should have used {% if comments.count == 0 %} instead
- Changed comment count display comments count

Comment form not working
- Comment submit button shows but no fields, on submit the url breaks
- changed { form|crispy } to {comment_form|crispy} which shows shows the comment field
- Form now submitting correctly

- Heroku not loading css, files are referrenced correctly in HTML locally. This must be an issue with heroku interpeting the location of css files
- Most answers on Stack Overflow static files not being located properly.
- Removed CollectStatic from Heroku and changed Debug from True to False.

# Unfixed Bugs

## Navigation bar
- Sticky navbar works for only a portion of the time, after a certain distance down the page it can be scrolled out of site.

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

- Recently Heroku had suspended automatic deployment so users will need to push directly from git using git push heroku main. You may have to recconet the repo to Heroku in which case go to Deploy, at the bottom will be the Deploy a GitHub branch section, input Main and press Deploy Branch.

# Credits

Useful websites and tutorials 
https://djangocentral.com/building-a-blog-application-with-django/
https://www.youtube.com/watch?v=B40bteAMM_M&list=PLCC34OHNcOtr025c1kHSPrnP18YPB-NFi&ab_channel=Codemy.com
https://www.samuelliedtke.com/blog/implement-comment-system-blog-application-django/#views
https://vegibit.com/slug-based-routing-in-django/

Bootstrap 
https://www.youtube.com/watch?v=qNifU_aQRio&ab_channel=AdrianTwarog
https://getbootstrap.com/docs/5.0/examples/pricing/
https://getbootstrap.com/

Django All Auth
https://django-allauth.readthedocs.io/en/latest/installation.html

## Content

pexels.com
googlefonts.com
fontawesome.com
pexels.com

## Media