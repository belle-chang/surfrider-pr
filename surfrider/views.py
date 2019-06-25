from django.shortcuts import render, redirect, render_to_response
from testing.models import BeachNameID, Beach
import datetime


# Create your views here.
def index(request):
    # if request.user.is_authenticated:
    #     return render(request, 'home.html')
    # # return HttpResponse("welcome.html")
    beach_dictionary = {}
    all_beaches = BeachNameID.objects.all()
    print(all_beaches)
    for beach in all_beaches:
        beach_dictionary[beach.beach_name] = Beach.objects.filter(beach_name=beach.beach_name).count()
    # {'beach_dict' : beach_dictionary}
    return render(request, 'welcome.html', {'beach_dict' : beach_dictionary})

# def reroute_to_surfrider(request, beach_id):
#     url = "https://www.surfrider.org/blue-water-task-force/beach/" + beach_id
#     if ()
#     return redirect(url)