from django.contrib.auth import get_user_model
from ninja_extra import api_controller, route, status
from ninja_extra.controllers import Detail, Id
from ninja_extra.pagination import (
    PageNumberPaginationExtra,
    PaginatedResponseSchema,
    paginate,
)
from ninja_extra.permissions import IsAuthenticated
from ninja_jwt.authentication import JWTAuth
from pydantic.types import UUID4

from bookstoreapi.apps.matters.mixins import MatterViewMixin
from bookstoreapi.apps.matters.models import Matter
from bookstoreapi.apps.matters.schemes.matters import MatterSchema
from bookstoreapi.apps.matters.schemes import CreateMatterSchema, MatterRetrieveSchema
from bookstoreapi.apps.matters.schemes.matters import (
    CreateMatterSchema, MatterUpdateSchema
)
# from bookstoreapi.apps.matters.tasks import process_subscription_notification
from bookstoreapi.apps.core.logger import logger


@api_controller("/matters", permissions=[IsAuthenticated], auth=JWTAuth())
class MattersController(MatterViewMixin):
    @route.post("", response=[Id, Detail(status_code=400)], url_name="create")
    def create_matter(self, matter: CreateMatterSchema):
        try:
            matter = matter.create_matter(owner=self.context.request.user)
            return self.Id(matter.pk)
        except Exception as ex:
            logger.error(f"failed to create matter: {ex}")
            return Detail(str(ex), status_code=400)

    @route.get(
        "",
        response=PageNumberPaginationExtra.get_response_schema(MatterRetrieveSchema),
        url_name="list",
    )
    @paginate(PageNumberPaginationExtra)
    def list_matters(self):
        return self.get_queryset()

    @route.get("/{uuid:matter_id}", response=MatterRetrieveSchema, url_name="detail")
    def retrieve_matter(self, matter_id: str):
        matter = self.get_object_or_exception(
            self.get_queryset(),
            id=matter_id,
            error_message="Matter with id {} does not exist".format(matter_id),
        )
        return matter

    @route.generic(
        "/{uuid:matter_id}",
        methods=["PUT"],
        response=MatterRetrieveSchema,
        url_name="update",
    )
    def update_matter(self, matter_id: str, matter_schema: MatterUpdateSchema):
        matter = self.get_object_or_exception(self.get_queryset(), id__exact=matter_id)
        matter_schema.update(matter)
        return matter

    @route.delete(
        "/{uuid:matter_id}", url_name="destroy", response=Detail(status_code=204)
    )
    def delete_matter(self, matter_id: str):
        matter = self.get_object_or_exception(
            self.get_queryset(),
            id=matter_id,
            error_message="Store with id {} does not exist".format(matter_id),
        )
        matter.delete()
        return self.create_response(
            "Item Deleted", status_code=status.HTTP_204_NO_CONTENT
        )

#
# @api_controller(
#     "/matters/{uuid:matter_id}", permissions=[IsAuthenticated], auth=JWTAuth()
# )
# class matterBookController(matterViewMixin):
#     User = get_user_model()
#     base_url = ""
#
#     @route.get(
#         "/books",
#         response=PaginatedResponseSchema[matterSchema],
#         url_name="books",
#     )
#     @paginate(PageNumberPaginationExtra)
#     def list_matter_books(self, matter_id: UUID4):
#         matters = matterBook.objects.filter(
#             matter_id=matter_id, matter__owner_id=self.context.request.user
#         )
#         return matters
#
#     @route.post(
#         "/book/create",
#         response=[(201, BookSchema), Detail(status_code=400)],
#         url_name="book-create",
#     )
#     def add_store_book(self, store_id: UUID4, book: CreateBookSchema):
#         try:
#             store = self.get_object_or_exception(
#                 Store,
#                 id=store_id,
#                 error_message="Store with id {} does not exist".format(store_id),
#             )
#             book = book.save(created_by=self.context.request.user)
#             StoreBook.objects.create(book=book, store=store)
#             return 201, book
#         except Exception as ex:
#             return self.create_response(
#                 str(ex), status_code=status.HTTP_400_BAD_REQUEST
#             )
#
#     def get_object(self, store_id: UUID4, book_id: UUID4):
#         store_book = self.get_object_or_none(
#             StoreBook.objects.select_related("store", "book"),
#             store__id=store_id,
#             book__id=book_id,
#             store__owner_id=self.context.request.user,
#         )
#         return store_book
#
#     @route.post(
#         "/book/{uuid:book_id}/borrow/{int:user_id}/",
#         response={200: BorrowOrReturnStoreBookSchema, 400: dict},
#         url_name="book-borrow",
#     )
#     def borrow_store_books(self, store_id: UUID4, book_id: UUID4, user_id: int):
#         store_book = self.get_object(store_id, book_id)
#
#         user = self.get_object_or_exception(
#             self.User,
#             id=user_id,
#             error_message="User with id {} does not exist".format(user_id),
#         )
#         if store_book.borrowed_by:
#             return self.create_response(
#                 message="Borrowed book can not be reassigned. It must be returned",
#                 status_code=status.HTTP_400_BAD_REQUEST,
#             )
#         store_book.borrowed_by = user
#         store_book.save()
#         return store_book
#
#     @route.post(
#         "/book/{uuid:book_id}/return",
#         response={200: StoreMessage, 400: StoreMessage},
#         url_name="book-return",
#     )
#     def return_store_books(self, store_id: UUID4, book_id: UUID4):
#         store_book = self.get_object(store_id, book_id)
#         if store_book.borrowed_by:
#             store_book.borrowed_by = None
#             store_book.save()
#             process_subscription_notification(store_book_id=store_book.id)
#             return status.HTTP_200_OK, StoreMessage(message="It is already returned")
#         return status.HTTP_400_BAD_REQUEST, StoreMessage(
#             message="It is already returned"
#         )
