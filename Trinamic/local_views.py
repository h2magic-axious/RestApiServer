from django.shortcuts import render

from Trinamic.models import Product, Category, Item
from FieldValue.models import Field
from Media.models import Media


def index(request):
    return render(request, 'BASE.html')


def product_center(request, p_id, c_id):
    product = Product.objects.get(pk=p_id)
    if c_id:
        category = Category.objects.get(pk=c_id)
    else:
        category_set = product.category_set.all()
        category = category_set[0] if category_set else None

    results = []

    if category and category.fields:
        fields = [Field.objects.get(pk=field) for field in category.fields.split(',') if field != '0']
        results.extend(field.alias for field in fields)

    context = {
        'product': product,
        'category': category,
        'category_fields': results
    }

    return render(request, 'Trinamic/ProductCenter.html', context=context)


def item_detail(request, item_id):
    item = Item.objects.get(pk=item_id)

    resources = {}
    for res_c in item.resourcecontent_set.all():
        alias = res_c.resource_type.alias
        if alias in resources:
            resources[alias].append(res_c)
        else:
            resources[alias] = [res_c]

    context = {
        'item': item,
        'fieldvalues': [(fv.field.alias, fv.value) for fv in item.fieldvalue_set.all()],
        'medis_list': Media.objects.filter(item__id=item_id, tag='CONTENT'),
        'resources': resources
    }
    return render(request, 'Trinamic/ItemDetail.html', context=context)
