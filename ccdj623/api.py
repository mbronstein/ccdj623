from ninja import NinjaAPI

#from events.api import router as events_router
from matters.api import router as matters_router
# from todos.api import router as todos_router

api = NinjaAPI()
api.add_router("/events/", events_router)

# api.add_router("/matters/", matters_router)
# api.add_router("/todos/", todos_router)