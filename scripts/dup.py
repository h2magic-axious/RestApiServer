import os, sys
import django
import json

from pathlib import Path

from googletrans import Translator

QINIU_DNS_NAME = 'http://tmc-item.chiplinkstech.com/'


def format_url(url: str):
    if url is None:
        return url

    filename = url.split('/')[-1]
    return QINIU_DNS_NAME + filename


class GTranslator:
    def __init__(self, host='translate.google.cn', dest='zh-CN'):
        self.__tr = Translator(service_urls=[host])
        self.__dest = dest

    def translate(self, text):
        try:
            print("Translating: ", text)
            return self.__tr.translate(text, self.__dest).text
        except:
            print("Translate failure")
            return text


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

pro = Path(r'E:\workspace\Trinamic\Memory\Trinamic_Json\map.json')

translator = GTranslator()

field_history = {field.name: field for field in Field.objects.all()}
resource_history = {res.name: res for res in ResourceType.objects.all()}

items = {item.model: item for item in Item.objects.all()}


# def get_field(name):
#     if name in field_history:
#         return field_history[name]
#     else:
#         field = Field.objects.create(name=name, alias=name)
#         field_history[name] = field
#         return field
#
#
# def get_resource_type(name):
#     if name in resource_history:
#         return resource_history[name]
#     else:
#         res_type = ResourceType.objects.create(name=name, alias=name)
#         resource_history[name] = res_type
#         return res_type
#
#
# model_list = {item.model: item for item in Item.objects.all()}
#
# with open(pro, 'r', encoding='utf-8') as f_painter:
#     data_list = json.load(f_painter)
#
# for model, detail in data_list.items():
#     item = model_list[model]
#     item.excerpt = translator.translate(detail['excerpt'])
#     item.save()