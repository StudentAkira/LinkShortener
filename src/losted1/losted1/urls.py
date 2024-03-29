from django.contrib import admin
from django.urls import path, include

from accounts.views import LoginView, RegistrateView, ShortegeView, LogoutView, StoregeView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('social_django.urls')),

    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('registrate/', RegistrateView.as_view()),
    path('shortege/', ShortegeView.as_view()),
    path('storage/', StoregeView.as_view()),

]
