"""student_management_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from student_management_system import settings
from student_management_app import views, HodViews

urlpatterns = [
    path("demo", views.showDemo),
    path("admin/", admin.site.urls),
    path("", views.showLoginPage),
    path("get_user_details/", views.GetUserDetails),
    path("logout_user", views.logout_user),
    path("doLogin", views.doLogin),
    path("admin_home", HodViews.admin_home),
    path("add_staff", HodViews.add_staff),
    path("add_staff_save", HodViews.add_staff_save),
    path("manage_staff", HodViews.manage_staff),
    path("edit_staff/<str:staff_id>", HodViews.edit_staff),
    path("add_course", HodViews.add_course),
    path("add_course_save", HodViews.add_course_save),
    path("manage_course", HodViews.manage_course),
    path("add_student", HodViews.add_student),
    path("add_student_save", HodViews.add_student_save),
    path("manage_student", HodViews.manage_student),
    path("add_subject", HodViews.add_subject),
    path("add_subject_save", HodViews.add_subject_save),
    path("manage_subject", HodViews.manage_subject),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

