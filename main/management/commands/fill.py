from django.core.management import BaseCommand

from main.models import Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        category_list = [
            {'name': 'Мандарины', 'discription': 'азиаткие'},
            {'name': 'Виноград', 'discription': 'Итальяский'},
            {'name': 'Ягода', 'discription': 'Лесная'}
        ]

        cotegory_for_create = []
        for category_item in category_list:
            cotegory_for_create.append(Category(**category_item))

        Category.objects.all().delete()
        Category.objects.bulk_create(cotegory_for_create)
