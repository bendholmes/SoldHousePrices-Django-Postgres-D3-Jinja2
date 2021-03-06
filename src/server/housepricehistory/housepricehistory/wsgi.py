"""
WSGI config for housepricehistory project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

#
# Copyright 2015 Benjamin David Holmes, All rights reserved.
#

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "housepricehistory.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
