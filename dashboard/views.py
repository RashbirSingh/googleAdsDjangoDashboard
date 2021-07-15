import os
from django.shortcuts import render



def dashboard(request):
    return render(request, "/Users/rashbirkohli/Desktop/staffing/DashboardGoogleAds/googleAdsDashboard/dashboard/templates/main.html")
