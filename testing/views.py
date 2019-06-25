from django.shortcuts import render, redirect
from .models import BeachNameID, Beach
import datetime
# Create your views here.
def reroute_to_surfrider(request, beach_id):
    url = "https://www.surfrider.org/blue-water-task-force/beach/" + str(beach_id)
    beach_obj = BeachNameID.objects.get(beach_id=beach_id)
    beach_name = beach_obj.beach_name

    beach_info = Beach(beach_name=beach_name,
                       date_visited=datetime.datetime.now()
                       )
    beach_info.save()
    return redirect(url)