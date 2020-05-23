from .models import User
from .serializers import UserSerializers
from .forms import SigninForm, SignupForm
from .constants import ACTION_SIGNUP, ACTION_USERNAME_CHECK, JWT_KEY
from  django.shortcuts import HttpResponse
from  rest_framework.views import APIView
from  rest_framework.response import Response
from  rest_framework_jwt.settings import api_settings
import json
import jwt
import datetime

jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_decode_handler = api_settings.JWT_DECODE_HANDLER

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

class TokenVerifyView(APIView):
    def post(self,request,*args,**kwargs):
        reply = {'status': False, 'msg': None}
        try:
            token = request.META.get('HTTP_AUTHORIZATION')
            if token == None:
                reply['status'] = False
                reply['msg'] = 'Token does not exist'
                return HttpResponse(json.dumps(reply))
            payload = jwt_decode_handler(token)
            reply['status'] = True
            reply['msg'] = 'Ok'
        except jwt.ExpiredSignature:
            reply['status'] = False
            reply['msg'] = 'Token has been expired'
        except:
            reply['status'] = False
            reply['msg'] = 'Token is invaild'
        return HttpResponse(json.dumps(reply))

class SigninView(APIView):
    def post(self,request,*args,**kwargs):
        reply = {'status': False, 'msg': None}
        decode_data = json.loads(request.body)
        signin_form = SigninForm(decode_data)
        print(fib(30)) # delay
        if signin_form.is_valid():
            username = signin_form.cleaned_data['username']
            password = signin_form.cleaned_data['password']
            try:
                user = User.objects.get(name=username)
                if user.password == password:
                    reply['status'] = True
                    reply['msg'] = 'Sign in successfully'
                    reply['user'] = username
                    payload = {
                        'user_id': user.pk,
                        'username': username,
                        'exp': (datetime.datetime.now() + api_settings.JWT_EXPIRATION_DELTA).timestamp()
                    }
                    token = jwt_encode_handler(payload)
                    reply['token'] = token
                    return HttpResponse(json.dumps(reply))
                else:
                    reply['status'] = False
                    reply['msg'] = 'Incorrect password'
            except:
                reply['status'] = False
                reply['msg'] = 'Invalid username'
        else:
            reply['status'] = False
            reply['msg'] = 'Invalid username or password'
        return HttpResponse(json.dumps(reply))

class SignupView(APIView):
    def post(self,request,*args,**kwargs):
        reply = {'status': True, 'msg': None}
        decode_data = json.loads(request.body)
        # action = request.POST.get('action') # www-form-urlencoded
        action = decode_data['action']
        # if action == "0": # www-form-urlencoded
        if action == ACTION_USERNAME_CHECK: # json
            username = decode_data['username']
            same_name_user = User.objects.filter(name=username)
            if same_name_user:
                reply['status'] = False
            else:
                reply['status'] = True
            return HttpResponse(json.dumps(reply))
        # elif action == "1": # www-form-urlencoded
        elif action == ACTION_SIGNUP: # json
            print(fib(30))
            # username = request.POST.get('username')
            # password = request.POST.get('password')
            username = decode_data['username']
            password = decode_data['password']
            try:
                new_user = User.objects.create()
                new_user.name = username
                new_user.password = password
                new_user.save()
                reply['status'] = True
            except:
                reply['status'] = False
                reply['msg'] = 'Error occured when creating account.'
            return HttpResponse(json.dumps(reply))

class LogoutView(APIView):
    def post(self,request,*args,**kwargs):
        reply = {'status': True, 'msg': None}
        return HttpResponse(json.dumps(reply))

class HomeView(APIView):
    def post(self,request,*args,**kwargs):
        print(fib(30))
        decode_data = json.loads(request.body)
        date = decode_data['date']
        print(date[5:])
        reply = {'status': True, 'msg': None}
        if date[5:] == '01-01':
            reply['msg'] = '元旦'
        elif date[5:] == '10-01':
            reply['msg'] = '国庆节'
        elif date[5:] == '12-25':
            reply['msg'] = '圣诞节'
        else:
            reply['status'] = False
        return HttpResponse(json.dumps(reply))
