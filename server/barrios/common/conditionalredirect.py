from django.shortcuts import redirect
from django_htmx.http import HttpResponseClientRedirect


def conditionalredirect(request, destination):
    if request.htmx:
        return HttpResponseClientRedirect(destination)
    else:
        return redirect(destination)
