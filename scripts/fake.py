import os, pathlib, random, sys
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ChiplinksWeb.settings")
django.setup()

from Trinamic.models import Product, Category, Item
from django.contrib.auth.models import User
from FieldValue.models import FieldValue, Field

BASE_DIR = pathlib.Path(__file__).parent.parent
sys.path.append(BASE_DIR)

words = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


def random_name(n=5):
    return ''.join(random.choice(words) for _ in range(n))


def random_text():
    return ''.join(random.choice(words) for _ in range(30))


def gen():
    Product.objects.all().delete()
    Category.objects.all().delete()
    Item.objects.all().delete()

    User.objects.all().delete()

    print("create a super user")
    User.objects.create_superuser('admin', 'admin@admin.com', 'admin')

    for pid in range(5):
        pro = random_name(3)
        print("create a product named: ", pro)
        p = Product.objects.create(name=pro, alias=random_name(), excerpt=random_text())
        for i in range(5):
            c = Category.objects.create(name=random_name(), product=p, alias=random_name(7), excerpt=random_text())
            print(f"create a category for {pro} named: ", c.name)
            for j in range(10):
                item = Item.objects.create(model=random_name(10), category=c, excerpt=random_text())
                print(f"create a item for {c.name} named: ", item.model)

    for fid in range(30):
        Field.objects.create(name=random_name(), alias=random_name(7))

    fields = [f.id for f in Field.objects.all()]
    items = [i.id for i in Item.objects.all()]
    for fvid in range(300):
        FieldValue.objects.create(field=random.choice(fields), value=random_name(10), item_id=random.choice(items))
