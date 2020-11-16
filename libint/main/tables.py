import django_tables2 as tables
from .models import Librarian, Book


class LibTable(tables.Table):
    id = tables.Column(verbose_name="id")
    family_lib = tables.Column(verbose_name="Фамилия")
    name_lib = tables.Column(verbose_name="Имя")
    patronymic_lib = tables.Column(verbose_name="Отчество")
    exp = tables.Column(verbose_name="Опыт работы")

    class Meta:
        model = Librarian
        template_name = "django_tables2/bootstrap.html"


class BookTable(tables.Table):
    id_book = tables.Column(verbose_name="id")
    name = tables.Column(verbose_name="Название книги")
    author = tables.Column(verbose_name="Автор")
    rate = tables.Column(verbose_name="Рейтинг книги")

    class Meta:
        model = Book
        template_name = "django_tables2/bootstrap.html"
