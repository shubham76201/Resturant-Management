from django.urls import path

from app1 import views
from . import views
from .views import (signupView,signinView,bookingView,BookTableView,bookView,imageuploadView)

urlpatterns = [
  
    path('signup',signupView.as_view(),name='signup'),
    path('',signinView.as_view(),name='signin'),
    path('signin',signinView.as_view(),name='signin'),
    path('booking',bookingView.as_view(),name='booking'),
     path('book_table',BookTableView.as_view(), name='book_table'),
     path('book',bookView.as_view(), name='book_table'),
     path('Order_Now1',views.Order_Now1,name='Order_Now1'),
     path('imageupload',imageuploadView.as_view(), name="imageupload")

]
