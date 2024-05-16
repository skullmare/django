from rest_framework.serializers import ModelSerializer
from main.models import event


class EventSerializer(ModelSerializer):
    class Meta:
        model = event
        fields = [
                    'id',
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