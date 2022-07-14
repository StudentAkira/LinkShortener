import requests
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.
from accounts.serializers import CustomUserSerializer


class LoginView(APIView):
    def get(self, request):
        if not request.user.is_authenticated:
            return render(request=request, template_name='login/login.html')
        return redirect('/shortege/')

    def post(self, request):
        username = request.POST.dict()['username']
        password = request.POST.dict()['password']
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('/shortege/')
        return redirect('/login/')


class LogoutView(APIView):

    def get(self, request):
        logout(request=request)
        return redirect('/login/')


class RegistrateView(APIView):
    def get(self, request):
        if not request.user.is_authenticated:
            return render(request=request, template_name='registrate/registrate.html')
        return redirect('/shortege/')

    def post(self, request):

        data = {
            'username': request.POST.dict()['username'],
            'password': make_password(request.POST.dict()['password']),
        }

        NewCustomUserSerializer = CustomUserSerializer(data=data)
        if NewCustomUserSerializer.is_valid():
            NewUser = NewCustomUserSerializer.create(validated_data=NewCustomUserSerializer.validated_data)
            return redirect('/login/')
        return redirect('/registrate/')


class ShortegeView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        return render(request=request, template_name='shortege/shortege.html', context={'username': request.user.username})


class ShowAvatarView(APIView):
    def get(self, request):
        user = request.user
        social = user.social_auth.get(provider='vk-oauth2')
        access_token = social.extra_data['access_token']
        response = requests.get(f'https://api.vk.com/method/users.get?fields=photo_100&v=5.131&access_token={access_token}')
        return Response({'user': response.json()})
