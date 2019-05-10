from django.test import TestCase

# Create your tests here.

from .models import Author, Book

class AuthorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        """
        create test
        """
        #Set up non-modified objects used by all test methods
        Author.objects.create(first_name='Aleksandr', last_name='Lenon')

    def test_first_name_label(self):
        """
        read test
        """
        author=Author.objects.get(id=1)
        # field_label = author.get_field('first_name').verbose_name
        field_label = author.first_name

        print("-----------------")
        print(field_label)
        print("-----------------")

        self.assertEquals(field_label, 'Aleksandr')

    def test_first_name_update(self):
        """
        update first_name test
        """
        author=Author.objects.get(id=1)
        # Author.objects.update(first_name='Aleksandr1')
        # здесь пока непонятно, как обновить поле (((
        Author.objects.filter(id=author.id).update(first_name='Aleksandr1')

        field_label = Author.first_name

        print("-----------------")
        print(field_label)
        print("-----------------")


        self.assertEquals(field_label, 'Aleksandr1')


    # def test_first_name_delete(self):
    #     author = Author.objects.get(id=1)
    #     author.delete()
    #     field_label = author.first_name
    #     self.assertEquals(field_label,'Aleksandr1')






# class BookModelTest(TestCase):
#     @classmethod
#     def setUpTestData(cls):
#         author = Author.objects.create(first_name='Aleksandr', last_name='Lenon')
#         Book.objects.create(author=author, title='Home', description='Home home', year_of_creating=1999)


#     def test_title_label(self):
#         title=Book.objects.get()
#         field_label = title._meta.get_field('title').verbose_name
#         self.assertEquals(field_label,'title')

#     def test_title_update(self):
#         pass

#     def test_title_delete(self):
#         pass

