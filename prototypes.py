"""

"""
import os
import sys

from django.conf import settings

"""
env dependent settings
"""
DEBUG = os.environ.get('DEBUG', 'on') == 'on'  # get debug flag from env, default on
SECRET_KEY = os.environ.get('SECRET_KEY', os.urandom(32))  # get secret_key from env, default 32 b rand
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '*').split(',')  # allowing all incoming traffic
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # base dir of app

settings.configure(
    DEBUG=DEBUG,  # using debug mode by default
    SECRET_KEY=SECRET_KEY,  # env dependent
    ALLOWED_HOSTS=ALLOWED_HOSTS,  # env dep
    ROOT_URLCONF='sitebuilder.urls',  # let sitebuilder manage urls
    TEMPLATES=(  # after Django 1.8, templates are defined in this manner
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [
                os.path.join(BASE_DIR, 'templates'),  # specify the template path
            ],
            'APP_DIRS': True,  # look for templates in app's dir
        },
    ),
    MIDDLEWARE_CLASSES=(),
    INSTALLED_APPS=(
        'django.contrib.staticfiles',
        'sitebuilder',  # the sitebuilder app
    ),
    STATIC_URL='/static/',
    SITE_PAGES_DIRECTORY=os.path.join(BASE_DIR, 'pages'),  # refers to pages for prototypes
    SITE_OUTPUT_DIRECTORY=os.path.join(BASE_DIR, '_build'),  # where to output statical site files
    STATIC_ROOT=os.path.join(BASE_DIR, '_build', 'static'),  # where to put static files of the statical site
    STATICFILES_STORAGE='django.contrib.staticfiles.storage.CachedStaticFilesStorage'  # for storing compressed static
)


"""
entry point
"""
if __name__ == "__main__":
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
