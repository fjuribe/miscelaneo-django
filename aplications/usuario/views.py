from rest_framework.views import APIView
from django.http import HttpResponse,JsonResponse
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
# Create your views here.


class Login(APIView):
    def post(self,request,format=None):
        # forma 1
        username=request.POST.get('username')
        password=request.POST.get('password')
        try:
            user=User.objects.get(username=username)
        except User.DoesNotExist:
            return HttpResponse(JsonResponse({"user":"No existe"}),content_type="application/json", status=404)

        pwd_valid=check_password(password,user.password)
        
        if not pwd_valid:
            print(pwd_valid)
            return HttpResponse(JsonResponse({"password":"contraseña invalida"}),content_type="application/json", status=404)
 
        token,created=Token.objects.get_or_create(user=user)
        # forma 2
        # user=User.objects.get(username='admin')
        # token=Token.objects.create(user=user)

        return HttpResponse(JsonResponse({"user":token.key}),content_type="application/json", status=201)
