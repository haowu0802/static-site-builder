from django.conf.urls import url

from .views import page

urlpatterns = (
    # matches pages with <slug>, 1 or more [a-zA-Z0-9_] and - , eg. /buy-now/
    url(r'^(?P<slug>[\w./-]+)/$', page, name='page'),
    url(r'^$', page, name='homepage'),
)