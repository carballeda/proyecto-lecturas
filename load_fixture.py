import os
import django
import json
from django.core.management import call_command

# Configura Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lecturas.settings")
django.setup()

# Cargar fixture
with open("libros_fixture.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Guardar en la base de datos
from django.core.serializers import deserialize
for obj in deserialize("json", json.dumps(data)):
    obj.save()

print("Datos cargados correctamente")