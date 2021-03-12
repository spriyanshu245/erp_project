
from django.shortcuts import HttpResponseRedirect, redirect, HttpResponse,Http404
from django.utils.deprecation import MiddlewareMixin
import re
LOGIN_PAGE ="/loginPage/"
ADMIN_RE="^/admin/*"
REGISTER_NEW_USER = "/register_new_user/"
class AuthRequiredMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.get_full_path() == LOGIN_PAGE or re.match(ADMIN_RE,request.get_full_path()):
            pass
        elif not request.user.is_authenticated :
            pass
            return HttpResponseRedirect(LOGIN_PAGE) # or http response
        return None

class AuthRequiredMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.get_full_path() == REGISTER_NEW_USER:
            if request.user.is_staff:
                pass
            else:
                return HttpResponse("<h3>You are not authorized to view this page</h3>")

