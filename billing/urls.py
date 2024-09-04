from django.contrib import admin
from django.urls import path,include
from . import views





urlpatterns = [
    path("base/calci", views.calci, name="calci"),
    path("bills",views.bills,name="bills"),
    path("taxpage",views.taxpage,name="taxpage"),
    path("dashboard",views.meterDashboard,name="dashboard"),
    path("",include('authentication.urls'))
   
        
   
    

    # path("/base",views.base)
]