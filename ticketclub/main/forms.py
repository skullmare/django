from .models import event, categories, seat
from django import forms
from django.forms import ModelForm, PasswordInput, TextInput, Textarea, DateInput, TimeInput, Select, ClearableFileInput, NumberInput, EmailInput
class EventAddForm(ModelForm):
    class Meta:
        model = event
        fields = [
                    'name',
                    'about_text',
                    'start_date',
                    'end_date',
                    'start_time',
                    'end_time',
                    'place',
                    'city',
                    'category',
                    'image'
                ]
        widgets = {
            'name': TextInput(
                attrs={
                    'class': 'form-control mb-2',
                    ' autocomplete': 'off'
                }
            ),
            'about_text': Textarea(
                attrs={
                    'class': 'form-control mb-2',
                    ' autocomplete': 'off'
                }
            ),
            'start_date': DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'type': 'date',
                    'class': 'form-control mb-2',
                    ' autocomplete': 'off'
                }
            ),
            'end_date': DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'type': 'date',
                    'class': 'form-control mb-2',
                    ' autocomplete': 'off'
                }
            ),
            'start_time': TimeInput(
                format=('%H-%m-%s'),
                attrs={
                    'type': 'time',
                    'class': 'form-control mb-2',
                    ' autocomplete': 'off'
                }
            ),
            'end_time': TimeInput(
                format=('%H-%m-%s'),
                attrs={
                    'type': 'time',
                    'class': 'form-control mb-2',
                    ' autocomplete': 'off'
                }
            ),
            'place': TextInput(
                attrs={
                    'class': 'form-control mb-2',
                    ' autocomplete': 'off'
                }
            ),
            'city': TextInput(
                attrs={
                    'class': 'form-control mb-2',
                    ' autocomplete': 'off'
                }
            ),
            'category': Select(
                choices=categories.objects.all(),
                attrs={
                    'class': 'form-control mb-2'
                }
            ),
            'image': ClearableFileInput()
            
        }
class EventUpdateForm(ModelForm):
    class Meta:
        model = event
        fields = [
                    'name',
                    'about_text',
                    'start_date',
                    'end_date',
                    'start_time',
                    'end_time',
                    'place',
                    'city',
                    'category',
                    'image'
                ]
        widgets = {
            'name': TextInput(
                attrs={
                    'id': 'id_name_update',
                    'class': 'form-control mb-2',
                    ' autocomplete': 'off'
                }
            ),
            'about_text': Textarea(
                attrs={
                    'id': 'id_about_text_update',
                    'class': 'form-control mb-2',
                    ' autocomplete': 'off'
                }
            ),
            'start_date': DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'id': 'id_start_date_update',
                    'type': 'date',
                    'class': 'form-control mb-2',
                    ' autocomplete': 'off'
                }
            ),
            'end_date': DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'id': 'id_end_date_update',
                    'type': 'date',
                    'class': 'form-control mb-2',
                    ' autocomplete': 'off'
                }
            ),
            'start_time': TimeInput(
                format=('%H-%m-%s'),
                attrs={
                    'id': 'id_start_time_update',
                    'type': 'time',
                    'class': 'form-control mb-2',
                    ' autocomplete': 'off'
                }
            ),
            'end_time': TimeInput(
                format=('%H-%m-%s'),
                attrs={
                    'id': 'id_end_time_update',
                    'type': 'time',
                    'class': 'form-control mb-2',
                    ' autocomplete': 'off'
                }
            ),
            'place': TextInput(
                attrs={
                    'id': 'id_place_update',
                    'class': 'form-control mb-2',
                    ' autocomplete': 'off'
                }
            ),
            'city': TextInput(
                attrs={
                    'id': 'id_city_update',
                    'class': 'form-control mb-2',
                    ' autocomplete': 'off'
                }
            ),
            'category': Select(
                choices=categories.objects.all(),
                attrs={
                    'id': 'id_category_update',
                    'class': 'form-control mb-2'
                }
            ),
            'image': ClearableFileInput()
            
        }
class SeatAddForm(ModelForm):
    class Meta:
        model = seat
        fields = [
                    'seat_no',
                    'price'
                ]
        widgets = {
            'seat_no': TextInput(
                attrs={
                    'class': 'form-control mb-2',
                    ' autocomplete': 'off'
                }
            ),
            'price': NumberInput(
                attrs={
                    'min': 0,
                    'class': 'form-control mb-2'
                }
            )
        }