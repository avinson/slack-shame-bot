"""
Django settings for slackbot project.

Generated by 'django-admin startproject' using Django 2.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ["SECRET_KEY"]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'slackbot',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'slackbot.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'slackbot.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

## app specific stuff
SLACK_API_TOKEN = os.environ["SLACK_API_TOKEN"]
GUIDE_URL = os.environ["GUIDE_URL"]
CHANNEL_MEMBER_THRESHOLD = os.environ["CHANNEL_MEMBER_THRESHOLD"]
REMIND_THRESHOLD = os.environ["REMIND_THRESHOLD"]
#REMIND_THRESHOLD = 0

# the initial etiquette guidelines to send a user
INITIAL_TEXT = f''':wave: I'm your friendly slack etiqeutte bot. Since you used `@here` or `@channel` in a channel with more than {CHANNEL_MEMBER_THRESHOLD} members, I'm passing along some guidelines here: {GUIDE_URL}
Please review the guidelines and consider avoiding the use of `@here` or `@channel` when possible as this can be disruptive or annoying to other employees.

Some examples of when `@channel` is appropriate:
* Update a project team's channel about a last-minute change in deadlines.
* Introduce a new employee or cross-functional partner to a channel.

Some examples of when `@here` is appropriate:
* You're locked out of the office and need help from someone already at work.

Examples of when using these keywords is *not* appropriate:
* There exists half a leftover sandwich in the kitchen.
* You brought back some treats from your trip (people can read scrollback for this).
* Miscellaneous office announcements that are not highly time sensitive (again, people can read the scrollback if interested).

Thanks for reading over this and being considerate. I'll send out another friendly reminder every {REMIND_THRESHOLD} days. Cheers!'''

# text to send after a period of REMIND_THRESHOLD days to refresh the user's memory
REMIND_TEXT = f''':wave: This is a friendly reminder to review the guidelines at {GUIDE_URL} and to consider whether you _really_ need to use an `@here` or `@channel` before posting.

Here's some examples of when using these keywords is *not* appropriate:
* There exists half a leftover sandwich in the kitchen.
* You brought back some treats from your trip (people can read scrollback for this).
* Miscellaneous office announcements that are not highly time sensitive (again, people can read the scrollback if interested).

Thanks!'''
