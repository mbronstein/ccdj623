from ninja import Router
from .models import Matter

router = Router()

@router.get('/')
def list_matters(request):
    return [
        {"id": m.id, "title": m.title}
        for m in Matter.objects.all()
        ]


