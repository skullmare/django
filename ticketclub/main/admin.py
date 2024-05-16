from django.contrib import admin

# Register your models here.
from main.models import client, event, ticket, ticket_status, categories, seat
# Register your models here.
admin.site.register(client)
admin.site.register(ticket)
admin.site.register(event)
admin.site.register(seat)
admin.site.register(ticket_status)
admin.site.register(categories)