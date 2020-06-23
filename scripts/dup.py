import os, sys
import django
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ChiplinksWeb.settings")
django.setup()

from Trinamic.models import Product, Category, Item
from MyUser.models import TmcUser
from FieldValue.models import FieldValue, Field
from Media.models import Media, MEDIA_TYPES, MEDIA_TAGS
from Resource.models import ResourceType, ResourceContent
from Blog.models import BlogCategory, BlogTag, BlogArticle, BlogComment

with open(r'Demo\TMC262-LA.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

obj = Item.objects.get(model=data['model'])
obj.excerpt = data['excerpt']

for media in data['media']:
    Media.objects.create(title=media['name'],
                         tag=media['tag'],
                         media_type=media['type'],
                         using_url=media['url'],
                         item=obj)

for field in data['fields']:
    f, v = field
    f_obj = Field.objects.get(name=f)
    FieldValue.objects.create(field=f_obj, value=v, item=obj)

for rt, rcs in data['resource'].items():
    rt_obj = ResourceType.objects.get(name=rt)
    for name, url in rcs:
        ResourceContent.objects.create(resource_type=rt_obj,
                                       name=name,
                                       using_url=url,
                                       item=obj)
