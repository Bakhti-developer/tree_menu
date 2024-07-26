from django import template
from django.urls import reverse, NoReverseMatch
from tree_menu.models import Menu, MenuItem

register = template.Library()

@register.inclusion_tag('tree_menu/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    menu = Menu.objects.get(name=menu_name)
    items = menu.items.select_related('parent').all()
    
    active_item = None
    for item in items:
        try:
            url = reverse(item.named_url) if item.named_url else item.url
            if request.path == url:
                active_item = item
                break
        except NoReverseMatch:
            continue

    def build_tree(items, parent=None):
        tree = []
        for item in items:
            if item.parent == parent:
                children = build_tree(items, item)
                tree.append((item, children))
        return tree

    tree = build_tree(items)
    return {'tree': tree, 'active_item': active_item, 'request': request}
