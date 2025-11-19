import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

username = os.getenv("DJANGO_SUPERUSER_USERNAME", "admin")
email = os.getenv("DJANGO_SUPERUSER_EMAIL", "ing_medina16@hotmail.com")
password = os.getenv("DJANGO_SUPERUSER_PASSWORD", "yktsadmin1234")

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password)
    print("Superusuario creado automáticamente.")
else:
    print("El superusuario ya existe.")
