from django.db import models


class Book(models.Model):
    id_book = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    author = models.CharField(max_length=50, blank=True, null=True)
    genre = models.IntegerField(blank=True, null=True)
    year_create = models.DateField(blank=True, null=True)
    price_book = models.IntegerField(blank=True, null=True)
    rate = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'book'


class Genre(models.Model):
    id_genre = models.BigAutoField(primary_key=True)
    name_genre = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'genre'


class LendingBooks(models.Model):
    code_lend = models.IntegerField(primary_key=True)
    id_librarian = models.IntegerField(blank=True, null=True)
    book = models.IntegerField(blank=True, null=True)
    reader = models.IntegerField(blank=True, null=True)
    date_lend = models.DateField(blank=True, null=True)
    expected_date = models.DateField(blank=True, null=True)
    actual_date = models.DateField(blank=True, null=True)
    sum_fine = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lending_books'


class Librarian(models.Model):
    id = models.BigAutoField(primary_key=True)
    family_lib = models.CharField(max_length=50, blank=True, null=True)
    name_lib = models.CharField(max_length=50, blank=True, null=True)
    patronymic_lib = models.CharField(max_length=50, blank=True, null=True)
    exp = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.family_lib

    class Meta:
        managed = False
        db_table = 'librarian'


class Reader(models.Model):
    id = models.BigAutoField(primary_key=True)
    family_read = models.CharField(max_length=50, blank=True, null=True)
    name_read = models.CharField(max_length=50, blank=True, null=True)
    patronymic_lib = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    num_mobile = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reader'


class SystemFine(models.Model):
    id_fine = models.BigAutoField(primary_key=True)
    fault_damage = models.CharField(max_length=50, blank=True, null=True)
    sum_fine = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'system_fine'
