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


if __name__ == '__main__':

    Product.objects.all().delete()
    Category.objects.all().delete()
    Item.objects.all().delete()

    User.objects.all().delete()

    print("create a super user")
    user = User.objects.create_superuser('admin', 'admin@admin.com', 'admin')

    product = ['IC', 'Drive', 'Module', 'PADdrive']
    for pro in product:
        print("create a product named: ", pro)
        p = Product.objects.create(name=product)
        for i in range(5):
            c = Category.objects.create(name=random_name(), product=p)
            print(f"create a category for {pro} named: ", c.name)
            for j in range(10):
                item = Item.objects.create(model=random_name(10), category=c)
                print(f"create a item for {c.name} named: ", item.model)
