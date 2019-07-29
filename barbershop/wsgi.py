"""
WSGI config for barbershop project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# TODO: Revisar si es necesario al hacer deploy
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'barbershop.settings.dev')

application = get_wsgi_application()
