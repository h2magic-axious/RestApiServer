import os, pathlib, random, sys
from datetime import timedelta

import django
import faker
from django.utils import timezone

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ChiplinksWeb.settings")
django.setup()

from Trinamic.models import Product, Category, Item
from django.contrib.auth.models import User

BASE_DIR = pathlib.Path(__file__).parent.parent
sys.path.append(BASE_DIR)

words = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


def random_name(n=5):
    return ''.join(random.choice(words) for _ in range(n))

def random_text():
    return ''.join(random.choice(words) for _ in range(30))

if __name__ == '__main__':

    Product.objects.all().delete()
    Category.objects.all().delete()
    Item.objects.all().delete()

    User.objects.all().delete()

    print("create a super user")
    user = User.objects.create_superuser('admin', 'admin@admin.com', 'admin')

    for pid in range(5):
        pro = random_name(3)
        print("create a product named: ", pro)
        p = Product.objects.create(name=pro, alias=random_name(5), excerpt=random_text())
        for i in range(5):
            c = Category.objects.create(name=random_name(), product=p, alias=random_name(7), excerpt=random_text())
            print(f"create a category for {pro} named: ", c.name)
            for j in range(10):
                item = Item.objects.create(model=random_name(10), category=c, excerpt=random_text())
                print(f"create a item for {c.name} named: ", item.model)
