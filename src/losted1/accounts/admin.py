from django.contrib import admin

# Register your models here.
from accounts.models import ShortedLink

admin.site.register(ShortedLink)
