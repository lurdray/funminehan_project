from django.contrib import admin
from .models import Outreach, Member, Event

# Register your models here.
admin.site.register(Outreach)
admin.site.register(Member)
admin.site.register(Event)
