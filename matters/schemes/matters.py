from typing import Optional

from djn_lomb1.matters.models import Matter
from bookstoreapi.apps.core.schema_fix import APIModelSchema
from bookstoreapi.apps.users.schema import UserRetrieveSchema



class MatterSchema(APIModelSchema):
    created_by: Optional[UserRetrieveSchema]

    class Config:
        model = Matter


class CreateMatterSchema(MatterSchema):
    class Config:
        model = Matter
        # optional = ["created_by"]

class MatterRetrieveSchema(APIModelSchema):
    pass

    class Config:
        model = Matter
        include = ["name", "id"]

class MatterUpdateSchema(APIModelSchema):
    pass

    class Config:
        model = Matter
        include = ["name", "id"]
