#-*- coding:utf8 -*-
from django.shortcuts import render
from django.contrib.auth import authenticate,login
from django.contrib.auth.backends import ModelBackend
# Create your views here.
from users.models import UserProfile
from django.db.models import Q
from django.views.generic import View
from django.contrib.auth.hashers import make_password


from users.forms.auth_form import LoginForm
from users.forms.reg_form import Regform
from utils.email_send import send_register_email
from users.models import EmailVerifyRecord

#email and username login
class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username = username)|Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None

#基于类
class LoginView(View):
    def get(self,request):

        return render(request, 'login/login.html', {})

    def post(self,request):

        login_form = LoginForm(request.POST)
        if login_form.is_valid():

            user_name = request.POST.get("username", "")
            pass_world = request.POST.get("password", "")

            user = authenticate(username=user_name, password=pass_world)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, 'main.html')
                else:
                    return render(request, 'login/login.html', {'msg': u"用户名密码错误"})
            else:
                return render(request, 'login/login.html', {'msg': u"用户名密码错误"})
        else:
            return render(request, 'login/login.html', {"login_form":login_form})


#基于函数
# def user_login(request):
#     if request.method == "POST":
#         user_name = request.POST.get("username","")
#         pass_world = request.POST.get("password","")
#
#         user = authenticate(username = user_name,password = pass_world)
#         if user is not None:
#             login(request,user)
#             return render(request,'main.html')
#         else:
#             return render(request, 'login/login.html',{'msg':u"用户名密码错误"})
#
#     elif request.method == 'GET':
#         return render(request,'login/login.html',{})

#reg
class RegisterView(View):

    def get(self,request):
        register_form = Regform()
        return render(request,'user/reguser.html', {'register_form':register_form})

    def post(self,request):
        register_form = Regform(request.POST)
        if register_form.is_valid():

            username = request.POST.get("email", "")
            pass_world = request.POST.get("password", "")

            if UserProfile.objects.filter(email=username):
                return render(request, 'user/reguser.html', {'register_form':register_form,'msg': u"用户已经注册"})

            user_profile = UserProfile()
            user_profile.username = username
            user_profile.email = username
            user_profile.is_active = False
            user_profile.password = make_password(pass_world)
            user_profile.save()

            send_register_email(username,"register")
            return render(request, 'login/login.html')
        else:
            return render(request, 'user/reguser.html',{'register_form':register_form})

#active
class ActiveUserView(View):
    def get(self,request,active_code):
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        if all_records:
            for record in all_records:
                email = record.email
                user = UserProfile.objects.get(email=email)
                user.is_active = True
                user.save()
        else:
            pass#render(request, 'fail_active.html')
        return render(request, 'login/login.html')









