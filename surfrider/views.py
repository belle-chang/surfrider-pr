from django.shortcuts import render, redirect, render_to_response
import datetime


# Create your views here.
def index(request):
    # if request.user.is_authenticated:
    #     return render(request, 'home.html')
    # # return HttpResponse("welcome.html")
    return render(request, 'welcome.html')

# def reroute_to_surfrider(request, beach_id):
#     url = "https://www.surfrider.org/blue-water-task-force/beach/" + beach_id
#     if ()
#     return redirect(url)