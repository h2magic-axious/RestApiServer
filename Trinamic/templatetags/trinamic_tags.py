from Trinamic.models import Product, Category, Item
from FieldValue.models import FieldValue
from Media.models import Media
from Resource.models import ResourceContent, ResourceType

from django import template

register = template.Library()


@register.simple_tag
def whole_product():
    return Product.objects.all()


@register.simple_tag
def seo_product_center(product_id):
    category_set = Category.objects.filter(product__id=product_id)
    content = ','.join(c.name for c in category_set)

    for category in category_set:
        items = ','.join(item.model for item in category.item_set.all())
        content += f',{items}'

    return content


@register.simple_tag
def category_set(product_id):
    return Category.objects.filter(product__id=product_id)


@register.simple_tag
def get_item_fieldvalue(item_id, field):
    try:
        fieldvalue = FieldValue.objects.get(item__id=item_id, field__alias=field)
        return fieldvalue.value
    except:
        return ''


@register.simple_tag
def get_item_media(item_id, tag, type_):
    try:
        media = Media.objects.get(item__id=item_id, tag=tag, media_type=type_)
        return media.using_url
    except:
        return ''
