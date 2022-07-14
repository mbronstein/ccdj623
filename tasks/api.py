# from ninja.main import Router
# from .models import Task
#
# router = Router()
#
#
# @router.get('/')
# def list_todos(request):
#     return [
#         {"id": e.id, "title": e.title}
#         for e in Task.objects.all()
#     ]
#
#
# @router.get('/{task_id}')
# def task_details(request, task_id: int):
#     task = Task.objects.get(id=task_id)
#     return {"title": task.title, "details": task.details}
