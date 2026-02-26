import os
import django

# Configura Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lecturas.settings")
django.setup()

from django.core.management import call_command
from django.contrib.auth import get_user_model

# Migraciones
call_command("migrate", interactive=False)

# Crear superusuario si no existe
User = get_user_model()
admin_username = os.getenv("DJANGO_ADMIN_USER")
admin_email = os.getenv("DJANGO_ADMIN_EMAIL")
admin_password = os.getenv("DJANGO_ADMIN_PASSWORD")

if admin_username and admin_email and admin_password:
    if not User.objects.filter(username=admin_username).exists():
        User.objects.create_superuser(admin_username, admin_email, admin_password)
        print(f"Superusuario {admin_username} creado.")
    else:
        print(f"Superusuario {admin_username} ya existe.")
else:
    print("Variables de entorno del superusuario incompletas. No se creó ningún usuario.")