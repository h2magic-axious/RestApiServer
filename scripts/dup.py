import os, sys
import django
import requests
from bs4 import BeautifulSoup

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

EXISTING_MODELS = [
    'TMC2300-LA',
    'TMC6300-LA',
    'TMC7300-LA',
    'TMC2041-LA',
    'TMC2100-LA',
    'TMC2100-TA',
    'TMC2130-LA',
    'TMC2130-TA',
    'TMC2202-WA',
    'TMC2208-LA',
    'TMC2209-LA',
    'TMC2224-LA',
    'TMC2226-SA',
    'TMC236B-PA',
    'TMC246B-PA',
    'TMC260A-PA',
    'TMC261A-PA',
]


def write_one(title, excerpt, title_picture, content_picture, fields, resources):
    try:
        item = Item.objects.get('title')
        item.excerpt = excerpt
        Media.objects.create(title=title, tag='TITLE', media_type='PICTURE', using_url=title_picture,
                             item=item)
        for index, media in enumerate(content_picture):
            if index:
                Media.objects.create(title=title + '-Pin', tag='CONTENT', media_type='PICTURE', using_url=media,
                                     item=item)
            else:
                Media.objects.create(title=title + '-Dia', tag='CONTENT', media_type='PICTURE', using_url=media,
                                     item=item)

        for k, v in fields.items():
            try:
                field = Field.objects.get(name=k)
            except:
                field = Field.objects.create(name=k, alias=k)

            FieldValue.objects.create(field=field, value=v, item=item)

        for res_t, res_c in resources.items():
            try:
                res_type = ResourceType.objects.get(name=res_t)
            except:
                res_type = ResourceType.objects.create(name=res_t, alias=res_t)

            for li_text, li_a in res_c:
                ResourceContent.objects.create(name=li_text, resource_type=res_type, using_url=li_a, item=item)

    except:
        print(title)
        return


with open('demo3.txt', 'r', encoding='utf-8') as f:
    models = [line.strip().split(';') for line in f]

for title, link in models:
    soup = BeautifulSoup(requests.get(link).content, 'lxml')
    body = soup.find(class_='article-content')
    excerpt = body.find('p').text.strip()
    figures = [figure.find('img')['src'] for figure in body.find_all('figure')]
    title_picture = figures[0]
    content_picture = figures[1:]

    tds = [[td.text.strip() for td in tbody.find('tr').find_all('td')] for tbody in body.find_all('tbody')]
    fields = dict()
    for k, v in tds:
        if k == '产品状态':
            k = 'Status'
        fields[k] = v

    resource_type_list = [h3.text for h3 in body.find_all('h3')]
    resource_content_list = [[(li.text, li.find('a')['href']) for li in ol.find_all('li')] for ol in
                             body.find_all('ol')]

    resources = {t: c for t, c in zip(resource_type_list, resource_content_list)}

    print(title, title_picture, content_picture)
