from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from student_management_app.EmailBackend import EmailBackend


def showDemo(request):
    return render(request, 'demo.html')


def showLoginPage(request):
    return render(request, "login_page.html")


def doLogin(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method not allowed</h2>")
    else:
        user = EmailBackend.authenticate(request, username=request.POST.get('email'),
                                         password=request.POST.get('password'))
        if user is not None:
            login(request, user)
            if user.user_type == "1":
                return HttpResponseRedirect('/admin_home')
            elif user.user_type == "2":
                return HttpResponse('Staff Login')
            else:
                return HttpResponse("Student Login")
        else:
            messages.error(request, "Invalid Login Details")
            return HttpResponseRedirect("/")


def GetUserDetails(request):
    if request.user is not None:
        return HttpResponse("User: " + request.user.email + " usertype: " + request.user.user_type)
    else:
        return HttpResponse("Please Login First")


def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/")
