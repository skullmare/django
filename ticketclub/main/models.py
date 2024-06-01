from django.db import models

class ticket_status(models.Model):
    name = models.CharField(max_length=30, blank=False)
    def __str__(self):
        return f'{self.name}'

class categories(models.Model):
    name = models.CharField(max_length=30, blank=False)
    def __str__(self):
        return f'{self.name}'
    
class participant(models.Model):
    name = models.CharField(max_length=30, blank=False)
    def __str__(self):
        return f'{self.name}'
    
class client(models.Model):
    email = models.CharField(max_length=256, blank=False)

    def __str__(self):
        return f'{self.email}'

class event(models.Model):
    name = models.CharField(max_length=30, blank=False)
    image = models.ImageField(upload_to='images/', max_length=300)
    about_text = models.CharField(max_length=500)
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    place = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    category = models.ForeignKey(categories, on_delete=models.CASCADE)
    participants = models.ManyToManyField(participant)
    def __str__(self):
            return f'{self.name}'

class seat(models.Model):
    seat_no = models.CharField(max_length=30, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    event = models.ForeignKey(event, on_delete=models.CASCADE)
    def __str__(self):
            return f'{self.event} {self.seat_no}'

class ticket(models.Model):
    ticket_no = models.CharField(max_length=20, blank=False)
    client = models.ForeignKey(client, on_delete=models.CASCADE)
    ticket_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.ForeignKey(ticket_status, on_delete=models.CASCADE, default=2)
    seat = models.ForeignKey(seat, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.ticket_no}'