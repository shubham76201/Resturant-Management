from django.shortcuts import render, redirect
from app1.models import Signup, Book_table
from django.contrib.auth.models import User, auth
from django.core.files.storage import FileSystemStorage
from .models import Order_Now
# Create your views here.


def signup(request):
    if request.method == "POST":
        username1 = request.POST.get('username1')
        first_name1 = request.POST.get('firstname1')
        email1 = request.POST.get('email')
        phone1 = request.POST.get('phone')
        password1 = request.POST.get('password')

        x = User.objects.create_user(
            username=username1, first_name=first_name1, email=email1, password=password1)
        x.save()
        print("User Created")
        return redirect('/')

    else:
        return render(request, 'signup.html')


def signin(request):
    if request.method == "POST":
        user1 = request.POST['uname']
        pass1 = request.POST['psw']

        user = auth.authenticate(username=user1, password=pass1)
        if user is not None:
            auth.login(request, user)
            return redirect('booking')
        else:
            return redirect('signin')
    else:
        return render(request, 'signin.html')


def booking(request):
    all_uploads = Order_Now.objects.all()
    return render(request, 'booking.html')


def book_table(request):
    return render(request, 'book_table.html')


def book(request):
    button = request.GET['b1']
    if button == "Book the Table":
        book1 = request.GET['book_id']
        name1 = request.GET['name']
        timeslot1 = request.GET['timeslot']
        table_no1 = request.GET['table_no']
        table_type1 = request.GET['table_type']
        date1 = request.GET['date']
        guest1 = request.GET['guest']
        date1 = request.GET['date']
        obj = Book_table.objects.create(booking_id=book1, name=name1, time_slot=timeslot1,
                                        table_no=table_no1, table_type=table_type1, guest_no=guest1, date=date1)
        return render(request, 'result.html', {'book2': book1, 'name': name1, 'time': timeslot1, 'table_type': table_type1, 'guest': guest1, 'table': table_no1, 'date': date1})

    if button == "Check for My Bookings":
        id = request.GET['book_id']
        obj = Book_table.objects.get(booking_id=id)
        msg = "Record Selected"
        return render(request, 'result.html', {'book2': id, 'name': obj.name, 'time': obj.time_slot, 'table_type': obj.table_type, 'guest': obj.guest_no, 'table': obj.table_no, 'id': obj.id})

    if button == "Update the Booking":
        id = request.GET['book_id']
        name1 = request.GET['name']
        timeslot1 = request.GET['timeslot']
        table_no1 = request.GET['table_no']
        table_type1 = request.GET['table_type']
        guest1 = request.GET['guest']
        obj = Book_table.objects.get(booking_id=id)
        obj.name = name1
        obj.time_slot = timeslot1
        obj.table_no = table_no1
        obj.table_type = table_type1
        obj.guest_no = guest1
        obj.save()
        msg = "Record Updated"
        return render(request, 'result.html', {'book2': id, 'name': obj.name, 'time': obj.time_slot, 'table_type': obj.table_type, 'guest': obj.guest_no, 'table': obj.table_no, 'id': obj.id})

    if button == "Delete the Booking":
        id = request.GET['book_id']
        obj = Book_table.objects.get(booking_id=id)
        obj.delete()
        msg = "Record Deleted" + obj.name
        return render(request, 'book_table.html', {'msg': msg})


def imageupload(request):
    button = request.POST['b1']
    if request.method == "POST" and request.FILES['myfile'] and button == "Book an Order":
           myfile = request.FILES['myfile']
           fs = FileSystemStorage()
           filename = fs.save(myfile.name, myfile)
           url = fs.url(filename)

           ordernow = Order_Now(
            order_id=request.POST.get('orderid'),
            name=request.POST.get('name'),
            gmail=request.POST.get('email'),
            Order_Snacks=request.POST.get('snack1'),
            Order_lunch=request.POST.get('lunch1'),
            Order_Beverages=request.POST.get('beverages1'),
            date1=request.POST.get('date1'),
            image=url)      
           ordernow.save()
           all_uploads = Order_Now.objects.all()
           #all_uploads.delete()

           return render(request, 'result1.html', {'uploads': all_uploads})
    else:
            return redirect('Order_Now1')


def Order_Now1(request):
    return render(request, 'order_now.html')
