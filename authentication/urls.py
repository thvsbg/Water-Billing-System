from django.contrib import admin
from django.urls import path,include
from . import views





urlpatterns = [
    path("",views.home,name="home"),
    path("signup",views.signup,name="signup"),
    path("signin",views.signin, name="signin"),
    path("doLogin",views.doLogin,name="doLogin"),
    path("base",views.base, name="base"),
    path("signout",views.signout,name="signout"),
    path("profile",views.profile,name="profile"),
    path("profile/update",views.update,name="update")
    

    # path("/base",views.base)
]
