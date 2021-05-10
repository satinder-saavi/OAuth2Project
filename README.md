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





<hr>
<hr>


# Django OAuth Toolkit
## https://django-oauth-toolkit.readthedocs.io/en/latest/



### Django OAuth Toolkit can help you by providing, out of the box, all the endpoints, data, and logic needed to add OAuth2 capabilities to your Django projects.

## Installation





### Install with pip
`pip install django-oauth-toolkit`

### Add oauth2_provider to your INSTALLED_APPS in your `settings.py`

```python
INSTALLED_APPS = (
    ...
    'oauth2_provider',
)
```

### If you need an OAuth2 provider you’ll want to add the following to your `urls.py`


```python
from django.urls import include, path

urlpatterns = [
    ...
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]
```

### Sync your database

`
python manage.py migrate oauth2_provider
`


## OAuth2 Authorization Grants

### An authorization grant is a credential representing the resource owner’s authorization (to access its protected resources) used by the client to obtain an access token.

####  Start the development server:

`python manage.py runserver`

#### Point your browser to http://127.0.0.1:8000/o/applications/register/ lets create an application.

### Fill the form as show in the screenshot bellow and before save take note of `Client id` and `Client secret` we will use it in a minute


### redirect uris must  be space seprated

Client id = `zyRqYcJoKj6ayWuXATBnottmd67AWOtyHvrGpswq`

Client secret =  `1hZI2eTiWDKR0Z0xyK3LvxBOeJReWORb181G4pDj1MGiOUbIBRpqYobQN4GV1DRiosdoUv5siZtktfl0n5K17cqMfkKTJuRNgJqn5oFgwaJOkRnSK4phXqKEdw4UJl4n`

![image-3.png](attachment:image-3.png)

#### To start the Authorization code flow go to this URL which is the same as shown below:

##### http://127.0.0.1:8000/o/authorize/?response_type=code&client_id=zyRqYcJoKj6ayWuXATBnottmd67AWOtyHvrGpswq&redirect_uri=http://127.0.0.1:8000/

![image.png](attachment:image.png)

### click on authorize redirect to redirect_uri with a code

#### http://127.0.0.1:8000/?code=h3QoizNE74WrF0tOTg7YQn1YwQytxq

### This is the OAuth2 provider trying to give you a code. in this case `h3QoizNE74WrF0tOTg7YQn1YwQytxq`

### Export it as an environment variable:

`export ID=zyRqYcJoKj6ayWuXATBnottmd67AWOtyHvrGpswq`


`export SECRET=1hZI2eTiWDKR0Z0xyK3LvxBOeJReWORb181G4pDj1MGiOUbIBRpqYobQN4GV1DRiosdoUv5siZtktfl0n5K17cqMfkKTJuRNgJqn5oFgwaJOkRnSK4phXqKEdw4UJl4n`


`export CODE=h3QoizNE74WrF0tOTg7YQn1YwQytxq`

#### Now that you have the user authorization is time to get an access token:

`curl -X POST \
    -H "Cache-Control: no-cache" \
    -H "Content-Type: application/x-www-form-urlencoded" \
    "http://127.0.0.1:8000/o/token/" \
    -d "client_id=${ID}" \
    -d "client_secret=${SECRET}" \
    -d "code=${CODE}" \
    -d "redirect_uri=http://127.0.0.1:8000/" \
    -d "grant_type=authorization_code"`

#### The OAuth2 provider will return the follow response:

{"access_token": "rkXLdj0xZXiwNK8NhzE7vR2vOdM5F2", "expires_in": 36000, "token_type": "Bearer", "scope": "read write", "refresh_token": "AJ9HjJ0xUUMd01M1T84c2rDLfWpEtg"}

#### To access the user resources we just use the access_token:

### Also for demo purpose you can
###  Test Your Authorization Server

#### http://django-oauth-toolkit.herokuapp.com/consumer/



# In case of error you may require corsheaders

# django-cors-headers
## https://github.com/adamchainz/django-cors-headers

### Installation

`pip install django-cors-headers`

### and then add it to your installed apps in `settings.py`


```python
INSTALLED_APPS = [
    ...
    'corsheaders',
    ...
]
```

### You will also need to add a middleware class to listen in on responses:

```python
MIDDLEWARE = [
    ...,
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    ...,
]
```

### also add some configurations in `settings.py` to allow cors on certian host instead of all

```python
CORS_ALLOW_ALL_ORIGINS=False
CORS_ALLOWED_ORIGINS = [
    "https://example.com",
    "https://sub.example.com",
    "http://localhost:8000",
    "http://localhost:8080",
    "http://localhost:5678",
    "http://127.0.0.1:8000",
    "http://127.0.0.1:8080",
    "http://127.0.0.1:5678",
]
```















<hr>
<hr>




# drf-yasg - Yet another Swagger generator

## https://drf-yasg.readthedocs.io/en/stable/readme.html


### Generate real Swagger/OpenAPI 2.0 specifications from a Django Rest Framework API.

### Installation

`pip install drf-yasg`

## In settings.py

```python
INSTALLED_APPS = [
   ...
   'django.contrib.staticfiles',  # required for serving swagger ui's css/js files
   'drf_yasg',
   ...
]
```

## In urls.py

```python
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

...

schema_view = get_schema_view(
   openapi.Info(
      title="USER API",
      default_version='v1',
      description="User API Endpoints",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
   url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   ...
]
```


### This exposes 4 endpoints:

#### A JSON view of your API specification at `/swagger.json`


#### A YAML view of your API specification at `/swagger.yaml`


#### A swagger-ui view of your API specification at `/swagger/`


#### A ReDoc view of your API specification at `/redoc/`
