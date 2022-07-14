from django.contrib import admin
from django.urls import path

from accounts.views import LoginView, RegistrateView, ShortegeView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('registrate/', RegistrateView.as_view()),
    path('shortege/', ShortegeView.as_view()),
]
