import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eagleinsight.settings')
django.setup()

# Import Django models
from Plate.models import Vehicle

# Example: Fetch and print all objects
objects = Vehicle.objects.all()
for obj in objects:
    print(obj.num_img)
