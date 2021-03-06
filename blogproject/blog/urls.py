from django.urls import path
from .views import *
from  . import views
app_name = 'blog'

urlpatterns = [
    path('detail/<int:id>', detail, name='detail'),
    path('new/', new, name='new'),
    path('create/', create, name='create'),
    path("update/<int:id>", update, name="update"),
    path('delete/<int:id>', delete, name="delete"),
    path('mustsign/', mustsign, name='mustsign'),
]