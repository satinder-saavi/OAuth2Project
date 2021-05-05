# OAuth2Project

#### Create a .env file for environment variables



#### Create a virtualenv 
`virtualenv venv`


#### Activate the env

##### linux
`source venv/bin/activate`

##### window
`venv\Scripts\activate`




## Now run following commands on activated virtualenv



## Make directories if not exists
`mkdir media static templates`


#### Install required packages
`pip install -r requirements.txt`


### Run makemigrations
`python manage.py makemigrations`

### Run migrate
`python manage.py migrate`



### Create superuser
`python manage.py createsuperuser`


### Django OAuth Toolkit 
#### https://django-oauth-toolkit.readthedocs.io/en/latest/tutorial/tutorial_01.html


##### test your app by visiting
##### http://django-oauth-toolkit.herokuapp.com/consumer/



### Django Swagger

##### Django REST Swagger (deprecated)
##### as https://django-rest-swagger.readthedocs.io/en/latest/ is `deprecated` as mention over here  https://github.com/marcgibbons/django-rest-swagger we are using 

#### drf-yasg - Yet another Swagger generator 
#### https://drf-yasg.readthedocs.io/en/stable/readme.html 