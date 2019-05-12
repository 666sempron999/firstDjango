from django.test import TestCase
from .models import Author, Book


class AuthorModelTest(TestCase):

    def setUp(self):
        """
        create test
        """
        Author.objects.create(first_name='Aleksandr', last_name='Lenon')

    def test_first_name_label(self):
        """
        read test
        """
        author = Author.objects.get(id=1)
        fieldLabel = author.first_name
        self.assertEquals(fieldLabel, 'Aleksandr')

    def test_first_name_update(self):
        """
        update first_name test
        """
        Author.objects.filter(id=1).update(first_name='Aleksandr1')

        author = Author.objects.get(id=1)
        fieldLabel = author.first_name
        self.assertEquals(fieldLabel, 'Aleksandr1')

    def test_first_name_delete(self):

        delData = Author.objects.get(id=1)
        delData.delete()

        try:
            # exception when author not exists
            author = Author.objects.get(id=1)
        except Exception as e:
            pass
        

class BookModelTest(TestCase):

    def setUp(self):
        author = Author.objects.create(first_name='Aleksandr', last_name='Lenon')
        Book.objects.create(author=author, title='Home', description='Home home', year_of_creating=1999)


    def test_title_label(self):
        title = Book.objects.get(id=1)
        fieldLabel = title._meta.get_field('title').verbose_name
        self.assertEquals(fieldLabel,'title')

    def test_title_update(self):

        bookFiled = Book.objects.get(id=1)
        bookFiled.title = 'Home alone'
        bookFiled.save()

        bookFiled = Book.objects.get(id=1)
        self.assertEquals(bookFiled.title, 'Home alone')


    def test_title_delete(self):
        delData = Book.objects.get(id=1).delete()

        try:
        # exception when title not exists
            bookFiled = Book.objects.get(id=1)
        except Exception as e:
            pass
