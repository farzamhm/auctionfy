from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Product)
admin.site.register(Bidder)
admin.site.register(Seller)
admin.site.register(UserProfile)

admin.site.register(
    Room,
    list_display=["id", "title", "staff_only"],
    list_display_links=["id", "title"],
)