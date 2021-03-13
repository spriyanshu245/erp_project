
from django.shortcuts import HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin
import re
LOGIN_PAGE ="/loginPage/"
ADMIN_RE="\/admin|\/login|\/logout|\/password_*|reset*"
class AuthRequiredMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.get_full_path() == LOGIN_PAGE or re.match(ADMIN_RE,request.get_full_path()):
            pass
        elif not request.user.is_authenticated :
            pass
            return HttpResponseRedirect(LOGIN_PAGE) # or http response
        return None
