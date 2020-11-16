from django.urls import path
from . import views

urlpatterns = [
    path('register', views.RegisterFormView.as_view(), name="register"),

    path('auth', views.LoginFormView.as_view(), name="auth"),

    path('', views.PersonListView.as_view(), name='home'),

    path('book', views.BookListView.as_view(), name='book'),

]
