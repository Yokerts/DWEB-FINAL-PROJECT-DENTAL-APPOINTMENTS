import os
import sys
from django.core.wsgi import get_wsgi_application

# Agregar carpeta 'app' al path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_wsgi_application()