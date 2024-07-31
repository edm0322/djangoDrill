from django.shortcuts import render
from burgers.models import Burger

def main(request):
    return render(request, "main.html")
    #return HttpResponse("Hi")


def burger_list(request):
    burgers = Burger.objects.all()
    print("전체 햄버거 목록", burgers)

    # Template를 이용하기 위해선 context Dict Type을 이용한다.
    context = {
        "burgers": burgers,
    }
    return render(request, "burger_list.html", context)
    #return HttpResponse("햄버거몇개")