import os, pathlib, random, sys
from datetime import timedelta

import django
import faker
from django.utils import timezone

BASE_DIR = pathlib.Path(__file__).parent.parent
sys.path.append(BASE_DIR)

if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE","ChiplinksWeb.settings")
    django.setup()