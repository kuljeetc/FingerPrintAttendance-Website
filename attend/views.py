from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

import datetime

from .models import Attendance
from .models import User
# Create your views here.

def index(request):
    user_list = User.objects.order_by('-user_id');
    context = { 'user_list': user_list }
    return render(request, 'attend/index.html', context)

def userattendance(request, inuser):
    attend_list = Attendance.objects.filter(user__user_id__iexact=inuser).order_by('-attend_date')
    username = get_object_or_404(User, pk=inuser).user_name

    context = { 'attend_list': attend_list, "user_name": username, "user_id": inuser }
    return render(request, 'attend/user.html', context)

@csrf_exempt
def adduser(request):
    try:
        print(request.POST)
        user_name = request.POST['user_name']
        print(user_name)
        user_password = request.POST['password']
    except (KeyError):
        return render(request, 'attend/add_user.html', {
            'error_message': 'Username or Password missing'
        })
    else:
        if User.objects.count() > 0:
            last_user_id = User.objects.order_by('-user_id').first().user_id;
        else:
            last_user_id = "S00000"
        
        user = User()
        user.password = user_password
        user.user_name = user_name
        new_user_id = str(int(last_user_id.replace('S', '0')) + 1)
        user.user_id = "S" + new_user_id.zfill(5)
        user.save()

        return render(request, "attend/add_user.html", {
            'user_id': user.user_id
        })

@csrf_exempt
def addattendance(request):
    try:
        user_id = request.POST['user_id'];
        print(user_id)
        user_password = request.POST['password'];
        print(user_password)
    except (KeyError):
        print('Userid or Password missing')
        return render(request, 'attend/add_attendance.html', {
            'error_message': 'Username or Password missing'
        })
    else:
        user = get_object_or_404(User, pk=user_id)
        
        attend = Attendance()
        attend.user = user
        attend.attend_date = datetime.datetime.now()
        attend.save()

        return render(request, "attend/add_user.html", {
            'user_id': user_id
        })
    
