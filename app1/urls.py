from django.urls import path

from app1 import views
from . import views

urlpatterns = [
    path('',views.signin, name='signin'),
    path('signup',views.signup,name='signup'),
     path('signin',views.signin,name='signin'),
     path('booking',views.booking,name='booking'),
     path('book_table',views.book_table, name='book_table'),
     path('book',views.book, name='book_table'),
     path('Order_Now1',views.Order_Now1,name='Order_Now1'),
     path('imageupload',views.imageupload, name="imageupload")

]
