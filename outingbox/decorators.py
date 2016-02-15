from django.http import JsonResponse
from .models import Activity

def require_user_authenticated(fn):
    def wrapper(request):
        if not request.user.is_authenticated():
            res = JsonResponse({'msg': 'not authenticated', 'status': '-1'})
            res.status_code = 400
            return res

        return fn(request)

    return wrapper

def require_activity(fn):
    def wrapper(request):
        activity_id = request.POST.get("id", None)
        if activity_id is None:
            res = JsonResponse({'msg': 'invalid id', 'status': '1'})
            return res

        try:
            activity = Activity.objects.get(pk=activity_id)
        except Activity.DoesNotExist:
            res = JsonResponse({'msg': 'invalid id', 'status': '1'})
            return res

        return fn(request, activity)

    return wrapper
