from typing import Any

from django.db.models import QuerySet

from .matters.models import Matter


class MatterViewMixin:
    request: Any

    def get_queryset(self) -> QuerySet:
        return Matter.objects.filter(owner_id=self.context.request.user)


class MatterQuerySetMixin:
    request: Any

    def get_queryset(self):
        pass
        # return StoreBookSubscription.objects.select_related(
        #     "store_book", "subscriber"
        # ).filter(store_book__store__owner=self.context.request.user)
