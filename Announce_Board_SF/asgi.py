import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Announce_Board_SF.settings')

application = get_asgi_application()
