"""
WSGI config for Proyecto_Final_de_BIOS_Python project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Proyecto_Final_de_BIOS_Python.settings')

application = get_wsgi_application()
