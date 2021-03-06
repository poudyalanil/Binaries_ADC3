from django.http import HttpResponse
from django.shortcuts import redirect


def admin(view_func):
    def wrapper_func(request, *args, **kwargs):
        # only is user is super user; can perform operation
        if request.user.is_superuser:
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponse("You are not allowed to view this page!!")
    return wrapper_func
