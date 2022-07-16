from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from .forms1 import EventForm


class EventView(View):
    form_class = EventForm
    initial = {'key': 'value'}
    template_name = 'event_template.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            return HttpResponseRedirect('/success/')

        return render(request, self.template_name, {'form': form})
