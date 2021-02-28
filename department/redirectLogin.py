
from django.shortcuts import HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin


class AuthRequiredMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.get_full_path() == "/":
            pass
        elif not request.user.is_authenticated:
            return HttpResponseRedirect('/') # or http response
        return None
