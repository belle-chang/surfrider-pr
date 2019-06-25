from django.shortcuts import render, redirect
from .models import BeachNameID, Beach
import datetime
# Create your views here.
def reroute_to_surfrider(request, beach_id):
    url = "https://www.surfrider.org/blue-water-task-force/beach/" + str(beach_id)
    print(str(beach_id))
    beach_obj = BeachNameID.objects.get(beach_id=beach_id)
    beach_name = beach_obj.beach_name
    print("beach obj" + beach_obj.beach_name)
    print("beach name" + beach_name)
    date_and_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
    # print("date and time" + date_and_time)

    beach_info = Beach(beach_name=beach_name,
                       date_visited=date_and_time,
                       )
    beach_info.save()
    return redirect(url)