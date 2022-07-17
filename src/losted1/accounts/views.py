import requests
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
from accounts.models import ShortedLink
from accounts.serializers import CustomUserSerializer, UrlSerializer


class LoginView(APIView):
    def get(self, request):
        if not request.user.is_authenticated:
            return render(request=request, template_name='login/login.html')
        return redirect('/shortege/')

    def post(self, request):
        username = request.POST.dict()['username']
        password = request.POST.dict()['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/shortege/')
        return redirect('/login/')


class LogoutView(APIView):

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/shortege/')
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

        new_custom_user_serializer = CustomUserSerializer(data=data)
        if new_custom_user_serializer.is_valid():
            new_custom_user_serializer.create(validated_data=new_custom_user_serializer.validated_data)
            return redirect('/login/')
        return redirect('/registrate/')


class ShortegeView(APIView):

    def get(self, request):
        user = request.user
        if not request.user.is_authenticated:
            return redirect('/login/')
        try:
            social = user.social_auth.get(provider='vk-oauth2')
            access_token = social.extra_data['access_token']
            response = requests.get(
                f'https://api.vk.com/method/users.get?fields=photo_100&v=5.131&access_token={access_token}')
            return render(request=request, template_name='shortege/shortege.html',
                          context={'username': request.user.username,
                                   'photo': response.json()['response'][0]['photo_100']})
        except:
            return render(request=request,
                          template_name='shortege/shortege.html',
                          context={'username': request.user.username})

    def post(self, request):
        try:
            url = ShortedLink.objects.get(long_url=request.POST.dict()['long_url'])
            url.users.add(request.user)
            return render(request=request, template_name='shortege/shortege.html',
                          context={'username': request.user.username,
                                   'short_url': url.short_url,
                                   'long_url': url.long_url})
        except ObjectDoesNotExist:
            data = {
                'long_url': request.POST.dict()['long_url'],
                'short_url': request.POST.dict()['long_url'],
                # first fill this param with long url value.
                # then, after creating raw in db - create this value using row`s id in db
            }

            new_url_serializer = UrlSerializer(data=data)
            if new_url_serializer.is_valid():
                new_url_serializer.create(validated_data=new_url_serializer.validated_data)
                new_url_db = ShortedLink.objects.get(long_url=data['long_url'])
                new_url_db.cut(urlid=new_url_db.id)
                new_url_db.users.add(request.user)
                new_url_db.save()
                return render(request=request,
                              template_name='shortege/shortege.html',
                              context={'username': request.user.username,
                                       'short_url': new_url_db.short_url,
                                       'long_url': new_url_db.long_url})

            return render(request=request,
                          template_name='shortege/shortege.html',
                          context={'username': request.user.username, 'error_message': 'url is invalid'})


class StoregeView(APIView):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('/login/')
        urls_db = ShortedLink.objects.filter(users=request.user)
        urls = []
        for url in urls_db:
           urls += [{'long_url': url.long_url, 'short_url': url.short_url}]
        return render(request=request,
                      template_name='storage/storage.html',
                      context={'urls': urls, 'username': request.user.username})
