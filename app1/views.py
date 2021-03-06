from django.shortcuts import render, redirect
from django.views import View
from app1.models import Signup, Book_table
from django.contrib.auth.models import User, auth
from django.core.files.storage import FileSystemStorage
from .models import Order_Now
# Create your views here.

class signupView(View):
  template_name="signup.html"
  def post(self,request):
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

  def get(self,request):
        return render(request, self.template_name)



class signinView(View):
  template_name="signin.html"
  def post(self,request):
    if request.method == "POST":
        user1 = request.POST['uname']
        pass1 = request.POST['psw']

        user = auth.authenticate(username=user1, password=pass1)
        if user is not None:
            auth.login(request, user)
            return redirect('booking')
        else:
            return redirect('signin')
  def get(self,request):
        return render(request, 'signin.html')
    
    
class bookingView(View):
  template_name="booking.html"
  def get(self,request):
    return render(request,self.template_name)

class BookTableView(View):
    template_name="book_table.html"
    def get(self,request):
     return render(request, self.template_name)


class bookView(View):
  template_name="result.html"
  def post(self,request):
    button = request.POST['b1']
    if button == "Book the Table" and request.method=="POST":
        book1 = request.POST['book_id']
        name1 = request.POST['name']
        timeslot1 = request.POST['timeslot']
        table_no1 = request.POST['table_no']
        table_type1 = request.POST['table_type']
        date1 = request.POST['date']
        guest1 = request.POST['guest']
        date1 = request.POST['date']
        obj = Book_table(booking_id=book1, name=name1, time_slot=timeslot1,
                                        table_no=table_no1, table_type=table_type1, guest_no=guest1, date=date1)
        obj.save()
        return render(request, self.template_name, {'book2': book1, 'name': name1, 'time': timeslot1, 'table_type': table_type1, 'guest': guest1, 'table': table_no1, 'date': date1})

    if button == "Check for My Bookings" and request.method=="POST":
        id = request.POST['book_id']
        obj = Book_table.objects.get(booking_id=id)
        msg = "Record Selected"
        return render(request, self.template_name, {'book2': id, 'name': obj.name, 'time': obj.time_slot, 'table_type': obj.table_type, 'guest': obj.guest_no, 'table': obj.table_no, 'id': obj.id})

    if button == "Update the Booking" and request.method=="POST":
        id = request.POST['book_id']
        name1 = request.POST['name']
        timeslot1 = request.POST['timeslot']
        table_no1 = request.POST['table_no']
        table_type1 = request.POST['table_type']
        guest1 = request.POST['guest']
        obj = Book_table.objects.get(booking_id=id)
        obj.name = name1
        obj.time_slot = timeslot1
        obj.table_no = table_no1
        obj.table_type = table_type1
        obj.guest_no = guest1
        obj.save()
        msg = "Record Updated"
        return render(request,self.template_name, {'book2': id, 'name': obj.name, 'time': obj.time_slot, 'table_type': obj.table_type, 'guest': obj.guest_no, 'table': obj.table_no, 'id': obj.id})

    if button == "Delete the Booking" and request.method=="POST":
        id = request.POST['book_id']
        obj = Book_table.objects.get(booking_id=id)
        obj.delete()
        msg = "Record Deleted" + obj.name
        return render(request, self.template_name, {'msg': msg})

class imageuploadView(View):
 template_name="result.html"  
 def post(self,request):
    button = request.POST['b1']
    if request.method == "POST"  and button == "Book an Order" and request.FILES['myfile']:
            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            image2 = fs.url(filename)

            order_id2=request.POST['orderid']
            name2=request.POST['name']
            gmail2=request.POST['email']
            Order_Snacks2=request.POST['snack1']
            Order_lunch2=request.POST['lunch1']
            Order_Beverages2=request.POST['beverages1']
            date12=request.POST['date1']
            distance=request.POST['distance']
            check = request.POST.get('take', 0)
            msg ="Order Booking Slip"
            msg1=""
            if check=="1":
                msg1="Your Order will be delivered Soon"
            else:
                msg1 ="Takeaway your Food after 30 min"
            
            all_uploads=Order_Now(order_id=order_id2 , name=name2, gmail=gmail2,Order_Snacks=Order_Snacks2,Order_lunch=Order_lunch2,Order_Beverages=Order_Beverages2,date1=date12,image=image2,Delivery=check,distance_from_home=distance)
            all_uploads.save()
            
            return render(request, 'result1.html',{'msg1':msg1,'msg':msg,'order_id':order_id2 , 'name':name2, 'gmail':gmail2,'Order_Snacks':Order_Snacks2,'Order_lunch':Order_lunch2,'Order_Beverages':Order_Beverages2,'date1':date12,'image':image2,'distance':distance})

    elif request.method == "POST" and button == "Check for Booked Order":

            id = request.POST['orderid']
            obj = Order_Now.objects.get(order_id=id)
            obj1=obj.Delivery
            msg ="Order Viewing Slip"
            if obj1==True:
                msg1="Your Order will be delivered in 30 min"
            else:
                msg1 ="Takeaway your Food after 30 min"
            
            return render(request, 'result1.html',{'msg1':msg1,'msg':msg,'order_id':id ,'name':obj.name,'gmail':obj.gmail,'Order_Snacks':obj.Order_Snacks,'Order_lunch':obj.Order_lunch,'Order_Beverages':obj.Order_Beverages,'date1':obj.date1,'image':obj.image,'distance':obj.distance_from_home})

    elif request.method == "POST" and request.FILES['myfile'] and button == "Update the Order":
            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            image2 = fs.url(filename)

            order_id2=request.POST['orderid']
            name2=request.POST['name']
            gmail2=request.POST['email']
            Order_Snacks2=request.POST['snack1']
            Order_lunch2=request.POST['lunch1']
            Order_Beverages2=request.POST['beverages1']
            date12=request.POST['date1']  
            id = request.POST['orderid']
            distance1=request.POST['distance']

            obj = Order_Now.objects.get(order_id=id)  
            obj.name = name2
            obj.gmail = gmail2
            obj.Order_Snacks = Order_Snacks2
            obj.Order_lunch = Order_lunch2
            obj.Order_Beverages = Order_Beverages2
            obj.Order_lunch = Order_lunch2
            obj.date1 = date12
            obj.image=image2
            obj.distance_from_home=distance1
            check = request.POST.get('take', 0)
        
            msg1=""
            if check=="1":
                obj.Delivery=True
                msg1="Your Order will be delivered Soon"
            else:
                obj.Delivery=False
                msg1 ="Takeaway your Food after 30 min"
            obj.save() 
            msg ="Order Updation Slip"
            return render(request, 'result1.html',{'msg1':msg1,'msg':msg,'order_id':id ,'name':obj.name,'gmail':obj.gmail,'Order_Snacks':obj.Order_Snacks,'Order_lunch':obj.Order_lunch,'Order_Beverages':obj.Order_Beverages,'date1':obj.date1,'image':obj.image,'distance':obj.distance_from_home})
    elif request.method == "POST" and request.FILES['myfile'] and button == "Delete my Order":
            id = request.POST['orderid']
            obj = Order_Now.objects.get(order_id=id)
            msg = obj.name 
            obj.delete()
            
            return render(request,'result2.html',{'msg':msg,'id':id})
    else:
            return redirect('Order_Now1')


def Order_Now1(request):
    return render(request, 'order_now.html')
