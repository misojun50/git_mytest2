from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from accountapp.models import HelloAgain


def hello_again(request):
    if request.method == "POST":

        temp = request.POST.get('input_text')

        hel_again = HelloAgain()
        hel_again.text = temp
        hel_again.save()

        hel_again_list = HelloAgain.objects.all()

        return render(request,'accountapp/hello_again.html',
                      context={'hel_again_list': hel_again_list })
    else:
        hel_again_list = HelloAgain.objects.all()
        return render(request, 'accountapp/hello_again.html',
                      context={'hel_again_list': hel_again_list })