import os
import shutil  # for using shell util
from django.conf import settings

from django.core.management import call_command  # for calling collectstatic
from django.core.management.base import BaseCommand, CommandError  # for building commands
from django.core.urlresolvers import reverse
from django.test.client import Client  # for requesting page content


def get_pages():
    """
    loop pages dir and yield page names, trim .html
    :return:
    """
    for name in os.listdir(settings.SITE_PAGES_DIRECTORY):
        if name.endswith('.html'):
            yield name[:-5]


class Command(BaseCommand):
    """
    implement Command
    """
    help = 'Build static site output.'

    def handle(self, *args, **options):
        """
        Request pages and build output.
        options: all pages, some pages, one page
        """
        settings.DEBUG = False  # to be able to use static file compress
        # if opt passed in, check for page existence
        if args:
            pages = args  # passed page names
            available = list(get_pages())  # get all existing pages
            invalid = []  # to store invalid pages
            for page in pages:
                if page not in available:
                    invalid.append(page)
            if invalid:
                msg = 'Invalid pages: {}'.format(', '.join(invalid))  # output invalid page names
                raise CommandError(msg)  # throw error with msg

        # when no arg gave
        else:
            # do all pages by default
            pages = get_pages()

            # checks output exist, if so, purge it, create new
            if os.path.exists(settings.SITE_OUTPUT_DIRECTORY):
                shutil.rmtree(settings.SITE_OUTPUT_DIRECTORY)  # rm _build
            os.mkdir(settings.SITE_OUTPUT_DIRECTORY)  # make _build
            os.makedirs(settings.STATIC_ROOT)  # make _build/static

            # call collectstatic command to copy all static files to _build/static
            call_command('collectstatic', interactive=False,
                         clear=True, verbosity=0)

            # loop pages, request each page, save content to static site _build
            client = Client()
            for page in pages:
                url = reverse('page', kwargs={'slug': page})
                response = client.get(url)  # request page content
                if page == 'index':  # put index at root of _build site
                    output_dir = settings.SITE_OUTPUT_DIRECTORY
                else:  # put other pages at _build/page/index.html
                    output_dir = os.path.join(settings.SITE_OUTPUT_DIRECTORY, page)
                    # some path may already exist, check for it before makedirs
                    if not os.path.exists(output_dir):
                        os.makedirs(output_dir)
                # write out files to output_dir
                with open(os.path.join(output_dir, 'index.html'), 'wb') as f:
                    f.write(response.content)
