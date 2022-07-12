from django.forms import ModelForm
from .models import Event

class EventForm(ModelForm):
    class Meta:
        model = Author
        # fields = ['title', 'category', 'matter', 'startdatetime', 'length',         'attendees', 'location', 'status']]
        fields = '__all__'