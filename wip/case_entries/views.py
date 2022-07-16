# from django.http import HttpResponseRedirect
# from django.shortcuts import get_object_or_404, render
# from django.urls import reverse
# from django.utils import timezone
# from django.views import generic
# from .models import CallEntry, NoteEntry, DocEntry, SmsEntry, DictationEntry
# from entries import forms, views, urls, templates
#
#
# from django.views.generic.edit import FormView
#
#
# class CallFormView(FormView):
#     template_name = 'CallFormVuew.html'
#     form_class = forms.CallForm
#     success_url = '/thanks/'
#
#     # def form_valid(self, form):
#     #     # This method is called when valid form data has been POSTed.
#     #     # It should return an HttpResponse.
#     #     form.send_email()
#     #     return super().form_valid(form)
