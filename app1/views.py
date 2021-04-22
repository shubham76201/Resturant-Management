from django.shortcuts import render, redirect
from app1.models import Signup,Book_table
from django.contrib.auth.models import User,auth

# Create your views here.


def signup(request):
    if request.method=="POST":
        username1= request.POST.get('username1')
        first_name1= request.POST.get('firstname1')
        email1= request.POST.get('email')
        phone1= request.POST.get('phone')
        password1= request.POST.get('password')
        
        x=User.objects.create_user(username=username1,first_name=first_name1,email=email1,password=password1)
        x.save()
        print("User Created")
        return redirect('/')

    else:
      return render(request,'signup.html')

def signin(request):
    if request.method=="POST":
      user1=request.POST['uname']
      pass1=request.POST['psw']

      user = auth.authenticate(username=user1,password=pass1)
      if user is not None:
          auth.login(request, user )
          return redirect('booking')
      else:
        return redirect('signin')
    else:
         return render(request,'signin.html')

def booking(request):
    return render(request,'booking.html')

def book_table(request):
    return render(request,'book_table.html')

def book(request):
    button=request.GET['b1']
    if button=="Book the Table":
        name1=request.GET['name']
        timeslot1=request.GET['timeslot']
        table_no1=request.GET['table_no']
        table_type1=request.GET['table_type']
        guest1=request.GET['guest']
        obj=Book_table.objects.create(name=name1,time_slot=timeslot1,table_no=table_no1,table_type=table_type1,guest_no=guest1)
        return render(request,'result.html',{'name':name1,'time':timeslot1,'table_type':table_type1,'guest':guest1,'table':table_no1})
        
        
    if button=="Check for My Bookings":
        id=request.GET['id']
        obj=Book_table.objects.get(pk=id)
        msg="Record Selected"
        return render(request,'result.html',{'name':obj.name,'time':obj.time_slot,'table_type':obj.table_type,'guest':obj.guest_no,'table':obj.table_no,'id':obj.id})

    if button=="Update the Booking":
        id=request.GET['id']
        name1=request.GET['name']
        timeslot1=request.GET['timeslot']
        table_no1=request.GET['table_no']
        table_type1=request.GET['table_type']
        guest1=request.GET['guest']
        obj=Book_table.objects.get(pk=id)
        obj.name=name1
        obj.time_slot=timeslot1
        obj.table_no=table_no1
        obj.table_type=table_type1
        obj.guest_no=guest1
        obj.save()
        msg="Record Updated"
        return render(request,'result.html',{'msg':msg,'name':obj.name,'time':obj.time_slot,'table_type':obj.table_type,'guest':obj.guest_no,'table':obj.table_no,'id':obj.id})
        
    if button=="Delete the Booking":
        id=request.GET['id']
        obj=Book_table.objects.get(pk=id)
        obj.delete()
        msg="Record Deleted" + obj.name
        return render(request,'book_table.html',{'msg':msg})
