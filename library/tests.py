from django.test import TestCase

# Create your tests here.

from .models import Author, Book

class AuthorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Author.objects.create(first_name='Aleksandr', last_name='Lenon')

    def test_first_name_label(self):
        author=Author.objects.get(id=1)
        field_label = author._meta.get_field('first_name').verbose_name
        self.assertEquals(field_label,'first name')


# class BookModelTest(TestCase):
#     @classmethod
#     def setUpTestData(cls):
#         Author.objects.create(first_name='Aleksandr', last_name='Lenon')
#         print("==========")
#         print(dir(Author))
#         print(str(Author.id))
#         print("==========")
#         Book.objects.create(author=1, title='Home', description='Home home', year_of_creating=1999)



#     def test_title_label(self):
#         title=Book.objects.get()
#         field_label = title._meta.get_field('title').verbose_name
#         self.assertEquals(field_label,'title')