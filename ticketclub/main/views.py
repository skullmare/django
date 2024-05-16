from django.shortcuts import render, redirect
import random, string
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import EventAddForm, SeatAddForm, EventUpdateForm
from .models import event, seat, ticket, client
from validate_email import validate_email
# Create your views here.
# -----------------------------------------index-------------------------------------------
def index_page(request):
    return render(request, 'index.html')
# -----------------------------------------events------------------------------------------
def events_page(request):
    search = request.GET.get('search')
    if request.GET.get('search'):
        events = event.objects.all().filter(name__icontains=search)
    else:
        events = event.objects.all()
    eventAdd = EventAddForm()
    eventUpdate = EventUpdateForm()
    if request.method == 'POST':
        try:
            event_id = request.POST['del_event_id']
            event.objects.filter(id=event_id).delete()
        except:
            None
        try:
            eventAdd = EventAddForm(request.POST,
                                    request.FILES)
            if eventAdd.is_valid():
                eventAdd.save()
        except:
            None
        return redirect('/events')
    return render(request, 'events.html', {'form': eventAdd,
                                           'form_update': eventUpdate,
                                           'events': events,
                                           'user': request.user})
# -----------------------------------------event-------------------------------------------
def event_page(request):
    seatAdd = SeatAddForm()
    


    # анализ поисковой строки
    id = request.GET.get('id')
    if request.GET.get('id'):
        events = event.objects.all().filter(id=id)
        if events.count() == 0:
            return redirect('/events')
    else:
        return redirect('/')
    

    if request.method == 'POST':
        if request.POST['seat_no'] and request.POST['price']:
            seatAdd = SeatAddForm(request.POST)
            if seatAdd.is_valid():
                seat.objects.create(seat_no=request.POST['seat_no'],
                                    price=request.POST['price'],
                                    event_id=int(id))
            return redirect(f'/event?id={id}')

    seats = seat.objects.raw(f'''
                    SELECT * FROM public.main_seat
                    where id not in (select seat_id from public.main_ticket)
                    and event_id = {id}
                        ''')
    return render(request, 'event.html', {'events': events,
                                          'user': request.user,
                                          'seats': seats,
                                          'seatAddForm': seatAdd,
                                          'event_id': id})
# -----------------------------------------register----------------------------------------
def register_page(request):
    if request.method == 'POST':
        if validate_email(request.POST['email']):
            try:
                user = User.objects.create_user(request.POST['email'],
                                                request.POST['email'],
                                                request.POST['password'])
                user.save()
                user = authenticate(username = request.POST['email'],
                                password = request.POST['password'])
                if user is not None:
                    login(request,user)
            except:
                return render(request, 'register.html', {'error': 'Такой email уже используется'})
            return redirect('/account')

    return render(request, 'register.html')
# -----------------------------------------account-----------------------------------------
def account_page(request):
    if request.method == 'POST':
        user = authenticate(username = request.POST['email'],
                             password = request.POST['password'])
        if user is not None:
            login(request,user)
        return redirect('/account')
    return render(request, 'account.html', {'user': request.user})
# -----------------------------------------logout------------------------------------------
def logout_view(request):
    logout(request)
    return redirect('/account')
# -----------------------------------------pay---------------------------------------------
@csrf_exempt
def pay_view(request):
    if (request.POST):
        if validate_email(request.POST['email']):
            sel_seats = request.POST['sel_seats']
            sel_seats = sel_seats.split(',')
            email = request.POST['email']
            try:
                client.objects.create(email=email)
            except:
                None
            for seat_id in sel_seats:
                if seat.objects.get(id=seat_id):
                    ticket.objects.create(ticket_no=generate_ticket_no(20),
                                        client_id=client.objects.get(email=email).id,
                                        ticket_amount=seat.objects.get(id=seat_id).price,
                                        seat_id=seat_id)
        return render(request, 'pay.html')
def generate_ticket_no(length):
    letters = string.ascii_uppercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string