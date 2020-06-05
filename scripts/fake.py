import os, random, sys
import django

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ChiplinksWeb.settings")
django.setup()

from Trinamic.models import Product, Category, Item
from MyUser.models import TmcUser
from FieldValue.models import FieldValue, Field
from Media.models import Media, MEDIA_TYPES, MEDIA_TAGS
from Resource.models import ResourceType, ResourceContent

words = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

MODELS = [
    Product,
    Category,
    Item,
    TmcUser,
    Field,
    FieldValue
]


def random_text(n=10):
    return ''.join(random.choice(words) for _ in range(n))


def clear_database():
    for model in MODELS:
        model.objects.all().delete()


def create_user():
    print("create a super user")
    TmcUser.objects.create_superuser('admin', 'admin@admin.com', 'admin')


def create_product(n=5):
    for _ in range(n):
        p_name = random_text(3)
        print("create a product named: ", p_name)
        Product.objects.create(name=p_name, alias=random_text(5), excerpt=random_text())


def create_category(n=5):
    for p in Product.objects.all():
        for _ in range(random.randint(0, n)):
            c_name = random_text(5)
            print('create category for ' + p.name + ' named ' + c_name)
            Category.objects.create(name=c_name, alias=random_text(), excerpt=random_text(), product=p)


def create_item(n=5):
    for c in Category.objects.all():
        for _ in range(random.randint(0, n)):
            i_name = random_text(7)
            print('category item for ' + c.name + ' named ', i_name)
            Item.objects.create(model=i_name, excerpt=random_text(10), category=c)


def create_field(n=30):
    for _ in range(n):
        f_name = random_text(3)
        print('category field named ' + f_name)
        Field.objects.create(name=f_name, alias=random_text(7))


def create_fieldvalue(n=10):
    # 获取所有字段的id表
    f_ids = [f.id for f in Field.objects.all()]
    # 遍历所有Item
    for i in Item.objects.all():
        # 随机抽取一批不重复的field.id
        fields = random.sample(f_ids, random.randint(0, n))
        for f_id in fields:
            print('category fieldvalue for ' + i.model)
            FieldValue.objects.create(field_id=f_id, value=random_text(5), item=i)


def create_media(n=20):
    items = [i.id for i in Item.objects.all()]
    for _ in range(n):
        title = random_text(3)
        print("create media: ", title)
        m_type = random.choice(MEDIA_TYPES)[0]
        m_tag = random.choice(MEDIA_TAGS)[0]
        Media.objects.create(title=title,
                             media_type=m_type,
                             tag=m_tag,
                             item_id=random.choice(items),
                             origin_url=f"http://{random_text(10)}",
                             using_url=f"http://{random_text(20)}"
                             )


def create_resource(n=10, m=50):
    res_types = [ResourceType.objects.create(name=random_text(3), alias=random_text(5)) for _ in range(n)]
    items = Item.objects.all()
    for _ in range(m):
        name = random_text(7)
        res_type = random.choice(res_types)
        item = random.choice(items)
        print("create resource content for ", res_type.alias, " named ", name)
        ResourceContent.objects.create(
            name=random_text(),
            origin_url=f"http://{random_text(10)}",
            using_url=f"http://{random_text(10)}",
            resource_type_id=res_type.id,
            item_id=item.id
        )


def gen():
    clear_database()

    create_user()
    create_product()
    create_category(7)
    create_item(10)
    create_field()
    create_fieldvalue()
    create_media()
    create_resource()


if __name__ == '__main__':
    gen()
