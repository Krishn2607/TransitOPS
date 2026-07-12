from functools import wraps
from django.http import HttpResponseForbidden

def allowed_roles(roles=[]):

    def decorator(view_func):

        @wraps(view_func)
        def wrapper(request, *args, **kwargs):

            if request.user.profile.role in roles:
                return view_func(request, *args, **kwargs)

            return HttpResponseForbidden(
                "<h2>You are not authorized to access this page.</h2>"
            )

        return wrapper

    return decorator