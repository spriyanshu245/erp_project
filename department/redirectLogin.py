
from django.shortcuts import HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin

LOGIN_PAGE ="/loginPage/"
class AuthRequiredMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.get_full_path() == LOGIN_PAGE:
            pass
        elif not request.user.is_authenticated :
            return HttpResponseRedirect(LOGIN_PAGE) # or http response
        return None
