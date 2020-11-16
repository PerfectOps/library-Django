from django.shortcuts import render
from .models import Librarian, Book
from django_tables2 import SingleTableView
from .tables import LibTable, BookTable
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login



def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/book.html')


class PersonListView(SingleTableView):
    model = Librarian
    table_class = LibTable
    template_name = 'main/index.html'


class BookListView(SingleTableView):
    model = Book
    table_class = BookTable
    template_name = 'main/book.html'


class RegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = '/'
    template_name = "main/register.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)


class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = "main/authent.html"
    success_url = "/"

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)
