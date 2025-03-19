from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User,auth
from django.contrib import messages
from home.models import Records
# Create your views here.


def register_view(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Thi Email Already exsits')
                return redirect('/register/')
            else:
                user = User.objects.create_user(first_name=first_name,
                last_name=last_name,email=email,username=username,
                password=password)
                user.set_password(password)
                user.save()
                return redirect('/')
        else:
            return render(request,'registration.html')

    return render(request,'registration.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            return redirect('/index/')
        else:
            messages.error(request,'Username or Password Incorrect')
            return redirect('/')
    return render(request,'login.html')



def index_view(request):
    patient_view = Records.objects.all().order_by('id')
    print(patient_view)
    context = {"datacollection" :patient_view}
    return render(request,'index.html',context)

def records_view(request):
    if request.method =='POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        phone_number = request.POST.get('phone_number')
        alternative_number = request.POST.get('alternative_number')
        email = request.POST.get('email')
        address = request.POST.get('address')
        dob = request.POST.get('dob')
        status = request.POST.get('status')
        next_meet = request.POST.get('next_meet')

        record = Records(name=name,age=age,phone_number=phone_number,
                     alternative_number=alternative_number,email=email,
                     address=address,dob=dob,
                     status=status,next_meet=next_meet)
        record.save()
        return redirect('/index/')


    return render(request,'records.html')


def delete_record(request, record_id):
    if request.method =='POST':
        record = get_object_or_404(Records, id=record_id)
        record.delete()
        return redirect('/index/')
    return redirect('/index/')
