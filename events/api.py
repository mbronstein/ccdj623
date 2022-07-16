# from ninja import Router
# from .models import Event
#
# router = Router()
#
#
# @router.get('/')
# def list_events(request):
#     return [
#         {"id": e.id, "date": e.compact_startdatetime, "title": e.title, 'length':e.length, "location":e.location},
#             "attendees":e.attendees,
#
#         for e in Event.objects.all()}
#     ]

#
# @router.get('/{event_id}')
# def event_details(request, event_id: int):
#     event = Event.objects.get(id=event_id)
#     return {"title": event.title, "details": event.details}
#
#
# startdatetime = models.DateTimeField(null=True)
#     length = models.IntegerField(default=30)
#     # EndDateTime = models.DateTimeField(null=True)
#     attendees = models.CharField(max_length=60, null=True, blank=True)
#     location = models.CharField(max_length=40, null=True, blank=True)
#     # status = models.ForeignKey("EventType", default='StatusType.OTHER',related_name="event_types")
#     created_date = models.DateField(default=timezone.now,
#                                     )
#
#     created_by = models.ForeignKey(USER_MODEL,
#                                    null=True,
#                                    related_name="event_created_by",
#                                    on_delete=models.CASCADE
#                                    )
#
#     assigned_to = models.ForeignKey(USER_MODEL,
#                                     default=1,
#                                     related_name="event_assigned_to",
#                                     on_delete=models.CASCADE,
#                                     )
#     note = models.TextField(blank=True,
#                             null=True
#                             )
#     priority = models.PositiveIntegerField(default=0
#                                            )