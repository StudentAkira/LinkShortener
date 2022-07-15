from django.contrib import admin
from django.urls import path, include

from accounts.views import LoginView, RegistrateView, ShortegeView, LogoutView, ShowAvatarView, NewUrl

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('social_django.urls')),

    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('registrate/', RegistrateView.as_view()),
    path('shortege/', ShortegeView.as_view()),

    path('showavatar/', ShowAvatarView.as_view()),
    path('test/', NewUrl.as_view()),
]
