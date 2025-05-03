from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from firstapp.forms import ReservationForm


# Create your views here.
def hello_world(request):
    return HttpResponse("Hello, world. Function Based View.")


class HelloView(View):
    def get(self,request):
        return HttpResponse("Hello, world. Class Based View.")


def home(request):
    form = ReservationForm()

    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Success")

    return render(request, 'index.html', {'form': form})