from django.contrib import admin
from django.urls import path

from accounts.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view()),
]
