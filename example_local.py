import os

ALLOWED_HOSTS = ['localhost', 'your.domain.name'];

# this is used as part of the auto-mailing services to identify where
# to redirect registration and password resets to
DOMAIN = 'your.domain.name'

# Leave this as true during development, so that you get error pages describing what went wrong
DEBUG = True

# You can add your e-mail if you want to receive notifications of failures I think , but its probably not a good idea
ADMINS = [
	#('Your Name', 'your_email@example.com'),
]

# You can also make local sqlite databases in your current directory
# if you want to test changes to the data model
DATABASES = {
    'default': {
      'ENGINE': 'django.db.backends.sqlite3',
      'NAME': 'db/testdb',
  },
}

PAYPAL_TEST = True

TIME_ZONE = 'America/New_York'

# set this to your site's prefix, This allows handling multiple deployments from a common url base
SITE_PREFIX = '/'

SECRET_KEY = 'IHaveNoIdeaWhatThisIsOrWhatItDoes'

STATICFILES_DIRS = (
  os.path.abspath('tracker/static/'),
);

STATIC_URL = "/static" + SITE_PREFIX
STATIC_ROOT = "/var/www/static" + SITE_PREFIX

HAS_GDOC = False
# GDOC_USERNAME = 'person@gmail.com'
# GDOC_PASSWORD = '12345678'

HAS_EMAIL = False
# EMAIL_HOST = 'mail.somwhere.com'
# EMAIL_PORT = 465
# EMAIL_HOST_USER = 'dude@somewhere.com'
# EMAIL_HOST_PASSWORD = '1234567878'
# EMAIL_FROM_USER = 'someone_else@somewhere.com'

HAS_GOOGLE_APP_ID = False
# GOOGLE_CLIENT_ID = 'the.google.apps.url.thingy'
# GOOGLE_CLIENT_SECRET = 'secretpasswordthing'

HAS_GIANTBOMB_API_KEY = False
# GIANTBOMB_API_KEY = 'Itsreallynicetohaveanditsfreetomakeanaccountbutnotneccessary'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

ADDITIONAL_APPS = [
    # place additional apps here
]
