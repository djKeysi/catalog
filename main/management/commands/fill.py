from django.core.management import BaseCommand

from main.models import Student


class Command(BaseCommand):
    def handle(self, *args, **options):
        #print('Hi,Sky!')
        student_list = [
            {'last_name':'Petrov','first_name':'Ivan'},
            {'last_name': 'Ivanov', 'first_name': 'Petr'},
            {'last_name': 'Semenov', 'first_name': 'Aleksandr'},
            {'last_name': 'Aleksandrov', 'first_name': 'Semen'},

        ]

        # for student_item in student_list:
        #     Student.objects.create(**student_item)

        student_fot_create=[]
        for student_item in student_list:
            student_fot_create.append(Student(**student_item))

        Student.objects.bulk_create(student_fot_create)

