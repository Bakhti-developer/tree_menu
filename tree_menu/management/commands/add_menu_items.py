from django.core.management.base import BaseCommand
from tree_menu.models import Menu, MenuItem

class Command(BaseCommand):
    help = 'Add menu items to the database'

    def handle(self, *args, **kwargs):
        menu, created = Menu.objects.get_or_create(name='main_menu')

        # Root items
        home_item, created = MenuItem.objects.get_or_create(
            menu=menu, name='Home', url='/', parent=None)
        
        about_item, created = MenuItem.objects.get_or_create(
            menu=menu, name='About', url='/about/', parent=None)
        
        services_item, created = MenuItem.objects.get_or_create(
            menu=menu, name='Services', url='/services/', parent=None)

        # Services sub-items
        web_dev_item, created = MenuItem.objects.get_or_create(
            menu=menu, name='Web Development', url='/services/web-development/', parent=services_item)
        
        seo_item, created = MenuItem.objects.get_or_create(
            menu=menu, name='SEO', url='/services/seo/', parent=services_item)
        
        # More complex items
        products_item, created = MenuItem.objects.get_or_create(
            menu=menu, name='Products', url='/products/', parent=None)

        electronics_item, created = MenuItem.objects.get_or_create(
            menu=menu, name='Electronics', url='/products/electronics/', parent=products_item)

        phones_item, created = MenuItem.objects.get_or_create(
            menu=menu, name='Phones', url='/products/electronics/phones/', parent=electronics_item)
        
        laptops_item, created = MenuItem.objects.get_or_create(
            menu=menu, name='Laptops', url='/products/electronics/laptops/', parent=electronics_item)
        
        accessories_item, created = MenuItem.objects.get_or_create(
            menu=menu, name='Accessories', url='/products/electronics/accessories/', parent=electronics_item)
        
        furniture_item, created = MenuItem.objects.get_or_create(
            menu=menu, name='Furniture', url='/products/furniture/', parent=products_item)

        chairs_item, created = MenuItem.objects.get_or_create(
            menu=menu, name='Chairs', url='/products/furniture/chairs/', parent=furniture_item)
        
        tables_item, created = MenuItem.objects.get_or_create(
            menu=menu, name='Tables', url='/products/furniture/tables/', parent=furniture_item)
        
        beds_item, created = MenuItem.objects.get_or_create(
            menu=menu, name='Beds', url='/products/furniture/beds/', parent=furniture_item)
        
        contact_item, created = MenuItem.objects.get_or_create(
            menu=menu, name='Contact', url='/contact/', parent=None)

        self.stdout.write(self.style.SUCCESS('Successfully added complex menu items'))
