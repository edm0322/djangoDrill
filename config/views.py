from django.shortcuts import render
from burgers.models import Burger

def main(request):
    return render(request, "main.html")
    #return HttpResponse("Hi")


def burget_list(request):
    burgers = Burger.objects.all()
    print("전체 햄버거 목록", burgers)
    return render(request, "burger_list.html")
    #return HttpResponse("햄버거몇개")