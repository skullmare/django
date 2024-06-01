from django.contrib import admin

# Register your models here.
from main.models import client, event, ticket, seat, participant
# Register your models here.
# admin.site.register(client)
@admin.register(client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'email',)
    list_display_links = ('email',)
    readonly_fields = ('email',)
    pass
@admin.register(ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('ticket_no',
                    'client',
                    'ticket_amount',
                    'status',
                    'seat')
    list_display_links = ('ticket_no',)
    readonly_fields = ('ticket_no',
                    'client',
                    'ticket_amount',
                    'status',
                    'seat',)
    search_fields = ('ticket_no',)
    list_filter = ('status',)
    pass
@admin.register(event)
class EventAdmin(admin.ModelAdmin):
    
    list_display = ('name',
                    'start_date',
                    'end_date',
                    'start_time',
                    'end_time',
                    'place',
                    'city',
                    'category',)
    date_hierarchy = ('start_date')
    list_display_links = ('name',)
    search_fields = ('name','place','city',)
    list_filter = ('start_date','city','category',)
    filter_horizontal = ('participants',)
    pass
@admin.register(seat)
class SeatAdmin(admin.ModelAdmin):
    list_display = ('seat_no',
                    'price',
                    'event',)
    search_fields = ('price',)
    list_display_links = ('seat_no',)
    list_filter = ('event',)
    readonly_fields = ('event',)
    pass
@admin.register(participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    pass