# Testing

## Validator Testing

CSS validation was passing fine initially, however after experiencing issues with Heroku loading the CSS file correctly whitenoise was implemented to correct this. Although it could be a seperate issue, since then the CSS file has thrown an error and multiple warnings. When checking via the site URL this is an issue however I have checked the CSS file by direct input.

### CSS 
Earlier CSS validator results
![CSS validator](https://res.cloudinary.com/ddxxrzq7g/image/upload/v1650972090/css_validator_index_rc6glx.png "CSS validator")

Post whitenoice CSS Validator
![CSS validator](https://res.cloudinary.com/ddxxrzq7g/image/upload/v1651238090/css_validation_error_xnukwq.png "CSS validator")

CSS Validated by direct input
![CSS validator](https://res.cloudinary.com/ddxxrzq7g/image/upload/v1651237653/css_direct_validation_splx9d.png "CSS validator")

------------------ 
### HTML

An occuring issue at the end of the project was failing HTML validation for seemingly no reason, when previously there were zero errors with all pages. The offending section was this line of code:

<pclass="card-text">{{ post.content | slice:":200" | safe }} < /p>

The p brackets are printed incorrectly above so the readme file doesn't hide them

removing the p tags removed all errors however created visible p tags on the actual site for the user to see. Removing some of the elements withint the brackets removed the errors also, even stranger changing from 200 to 100 also removed the errors. Some of the issues I experienced could not be replicated afterwards which is very strange.

HTML index page validator
![HTML index validator](https://res.cloudinary.com/ddxxrzq7g/image/upload/v1650972457/HTML_Index_Validator_lbitjw.png "HMTL index validator")

HTML register page validator
![HTML register validator](https://res.cloudinary.com/ddxxrzq7g/image/upload/v1651239708/HTML_register_validation_m3eaua.png "HTML register validator")

HTML add post page validator
![HTML add post validator](https://res.cloudinary.com/ddxxrzq7g/image/upload/v1650972461/HTML_Add_Post_Validation_mozpd7.png "HTML index validator")

HTML open post page validator
![HTML open post validator](https://res.cloudinary.com/ddxxrzq7g/image/upload/v1651242017/html_open_post_validation_e1m7bf.png "HTML open post validator")

HTML Profile validator
![HTML Profile validator](https://res.cloudinary.com/ddxxrzq7g/image/upload/v1651090456/HTML_Profile_Validator_bdyshi.png "HTML profile validator")

HTML Logout validator
![HTML Logout validator](https://res.cloudinary.com/ddxxrzq7g/image/upload/v1650972715/HTML_logout_Validator_cmtgge.png "HTML logout validator")

HTML Login validator
![HTML Login validator](https://res.cloudinary.com/ddxxrzq7g/image/upload/v1650973140/HTML_Login_Validation_gozobo.png "HTML login validator")

HTML Password Reset Validator
![HTML password reset validator](https://res.cloudinary.com/ddxxrzq7g/image/upload/v1651242017/html_password_reset_validation_t6oa1n.png "HTML  validator")

HTML Password Change Validator
![HTML password change validator](https://res.cloudinary.com/ddxxrzq7g/image/upload/v1651242017/html_password_change_validation_hxigyj.png "HTML  validator")

HTML Email Address' Validator
![HTML email validator](https://res.cloudinary.com/ddxxrzq7g/image/upload/v1651242350/html_email_validaton_xmadfk.png "HTML email validator")

------------------ 
### Python

In the blog folder

Admin Validator
![admin.py validator](https://res.cloudinary.com/ddxxrzq7g/image/upload/v1651244031/python%20validation/blog%20py/admin_py_nncgo8.png "admin.py validator image")

Apps Validator
![apps.py validator](https://res.cloudinary.com/ddxxrzq7g/image/upload/v1651244031/python%20validation/blog%20py/apps_py_vv9zxf.png "apps.py validator image")

Forms Validator
![forms.py validator](https://res.cloudinary.com/ddxxrzq7g/image/upload/v1651244031/python%20validation/blog%20py/apps_py_vv9zxf.png "forms.py validator image")

Models Validator
![models.py validator](https://res.cloudinary.com/ddxxrzq7g/image/upload/v1651244030/python%20validation/blog%20py/models_py_vv8jgi.png "models.py validator image")

Urls Validator
![urls.py validator](https://res.cloudinary.com/ddxxrzq7g/image/upload/v1651244030/python%20validation/blog%20py/urls_py_hdcr2m.png "urls.py validator image")

Views Validator
![views.py validator](https://res.cloudinary.com/ddxxrzq7g/image/upload/v1651244030/python%20validation/blog%20py/views_py_zueblg.png "views.py validator image")

-------
In the gardengnome folder

Asgi Validator
![asgi.py validator](https://res.cloudinary.com/ddxxrzq7g/image/upload/v1651244030/python%20validation/garden%20gnome%20py/asgi_py_w0vwst.png "asgi.py validator image")

Settings Validator: This validator is showing lines are too long however this physically cannot be avoided.
![settings.py validator](https://res.cloudinary.com/ddxxrzq7g/image/upload/v1651244031/python%20validation/garden%20gnome%20py/settings_failed_py_v613oa.png "settings.py validator image")

Urls Validator
![urls.py validator](https://res.cloudinary.com/ddxxrzq7g/image/upload/v1651244029/python%20validation/garden%20gnome%20py/urls_y_mddulm.png "urls.py validator image")

Wsgi Validator
![wsgi.py validator](https://res.cloudinary.com/ddxxrzq7g/image/upload/v1651244030/python%20validation/garden%20gnome%20py/wsgi_py_qzn8n6.png "wsgi.py validator image")

------
General Files

Manage Validator
![manage.py validator](https://res.cloudinary.com/ddxxrzq7g/image/upload/v1651244030/python%20validation/manage_py_n09obi.png "manage.py validator image")

Env Validator: As with the settings file this validator is showing lines are too long when this physically cannot be avoided.
![env.py validator](https://res.cloudinary.com/ddxxrzq7g/image/upload/v1651244031/python%20validation/env_failed_py_c6robb.png "env.py validator image")

