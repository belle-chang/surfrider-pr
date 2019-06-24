from django.shortcuts import render, redirect, render_to_response


# Create your views here.
def index(request):
    # if request.user.is_authenticated:
    #     return render(request, 'home.html')
    # # return HttpResponse("welcome.html")
    return render(request, 'welcome.html')