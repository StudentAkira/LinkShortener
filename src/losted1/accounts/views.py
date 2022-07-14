from django.shortcuts import render
from rest_framework.views import APIView


# Create your views here.
class LoginView(APIView):
    def get(self, request):
       return render(request=request, template_name='login/login.html')
