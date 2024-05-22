from django.contrib import admin

# Register your models here.
from main.models import client, event, ticket, seat
# Register your models here.
# admin.site.register(client)
@admin.register(client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'email')
@admin.register(ticket)
class TicketAdmin(admin.ModelAdmin):
    pass
@admin.register(event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'about_text',
                    'start_date',
                    'end_date',
                    'start_time',
                    'end_time',
                    'place',
                    'city',
                    'category')
@admin.register(seat)
class SeatAdmin(admin.ModelAdmin):
    pass
# admin.site.register(ticket)
# admin.site.register(event)
# admin.site.register(seat)