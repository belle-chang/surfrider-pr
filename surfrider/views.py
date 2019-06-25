from django.shortcuts import render, redirect, render_to_response
from testing.models import BeachNameID, Beach
import datetime


# Create your views here.
def index(request):
    # if request.user.is_authenticated:
    #     return render(request, 'home.html')
    # # return HttpResponse("welcome.html")
    beach_dictionary = {}
    beach_ids = {}
    all_beaches = BeachNameID.objects.order_by('beach_name').all()
    print(all_beaches)
    for beach in all_beaches:
        beach_dictionary[beach.beach_name] = Beach.objects.filter(beach_name=beach.beach_name).count()
        beach_ids[beach.beach_name] = beach.beach_id
    # {'beach_dict' : beach_dictionary}
    return render(request, 'welcome.html', {'beach_dict': beach_dictionary, 'beach_ids' : beach_ids})

def see_stats(request, beach_id):
    current_beach = BeachNameID.objects.get(beach_id=beach_id)
    err_msg = ""
    beach_name = current_beach.beach_name
    current_stats = Beach.objects.filter(beach_name=beach_name).order_by('-date_visited').values()
    if current_stats.count() == 0:
        err_msg = "Sorry, no data to show at this time!"
    print(current_stats)
    return render(request, 'stats.html', {'stats': current_stats, 'err_msg': err_msg})

def clear_db(request):
    Beach.objects.all().delete()
    return index(request)

# def reroute_to_surfrider(request, beach_id):
#     url = "https://www.surfrider.org/blue-water-task-force/beach/" + beach_id
#     if ()
#     return redirect(url)