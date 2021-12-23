from django.test import TestCase

from ..models import Person

class PersonModelClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        Person.objects.create(
            rank='1stLt',
            lname="Doe",
            fname="John",
            branch="USMC",
            category="Active Duty member",
            edipi="1234567890"
        )

    def test_rank_label(self):
        person = Person.objects.get(id=1)
        field_label = person._meta.get_field('rank').verbose_name
        self.assertEqual(field_label, 'rank')

    def test_lname_label(self):
        person = Person.objects.get(id=1)
        field_label = person._meta.get_field('lname').verbose_name
        self.assertEqual(field_label, 'lname')

    def test_fname_label(self):
        person = Person.objects.get(id=1)
        field_label = person._meta.get_field('fname').verbose_name
        self.assertEqual(field_label, 'fname')

    def test_branch_label(self):
        person = Person.objects.get(id=1)
        field_label = person._meta.get_field('branch').verbose_name
        self.assertEqual(field_label, 'branch')

    def test_category_label(self):
        person = Person.objects.get(id=1)
        field_label = person._meta.get_field('category').verbose_name
        self.assertEqual(field_label, 'category')

    def test_edipi_label(self):
        person = Person.objects.get(id=1)
        field_label = person._meta.get_field('edipi').verbose_name
        self.assertEqual(field_label, 'edipi')

    def test_rank_fullname(self):
        person = Person.objects.get(id=1)
        expected_object_name = f'{person.rank} {person.lname}, {person.fname}'
        self.assertEqual(str(person), expected_object_name)