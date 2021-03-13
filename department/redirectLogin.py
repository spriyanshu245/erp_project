
from django.shortcuts import HttpResponseRedirect, redirect, HttpResponse,Http404
from django.utils.deprecation import MiddlewareMixin
import re
LOGIN_PAGE ="/loginPage/"

ADMIN_RE="\/admin|\/login|\/logout|\/password_*|reset*"
REGISTER_NEW_USER = "/register_new_user/|/register"

class AuthRequiredMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.get_full_path() == LOGIN_PAGE or re.match(ADMIN_RE,request.get_full_path()):
            pass
        elif not request.user.is_authenticated :
            pass
            return HttpResponseRedirect(LOGIN_PAGE)
        if re.match(REGISTER_NEW_USER,request.get_full_path()) and not request.user.is_staff:
                return HttpResponse("<h3>You are not authorized to view this page</h3>")
         # or http response
        return None

        

